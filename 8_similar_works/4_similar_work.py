import pandas as pd
import numpy as np
import copy
from csv import writer

work_prf = pd.read_csv(r"./indeces_of_tags.csv")
test_data = pd.read_csv(r"./testResultData.csv")

jacard_sim = list()
tt = 0
    
test_data = test_data['workId'].tolist()

for i in test_data:
    wrk = work_prf.loc[work_prf['question_id'] == i]
    if wrk.empty == True:
        continue

    wrk_id = i
    wrk_tags = wrk.iloc[:, 1:]

    wrk_tags = np.array(wrk_tags.values[0].tolist())
    wrk_tags = (wrk_tags[np.logical_not(np.isnan(wrk_tags))]).tolist()

    #################### similarity between question and requester
    for other_wrk in work_prf.iterrows():
        sim_wrk_id = other_wrk[1]['question_id']
        other_wrk = np.array(other_wrk[1].values.tolist())
        other_wrk = (other_wrk[np.logical_not(np.isnan(other_wrk))]).tolist()
        other_wrk = other_wrk[1:]

        if (len(wrk_tags) == 0) | (len(other_wrk) == 0):
            continue

        i=set.intersection(set(wrk_tags),set(other_wrk))

        res = 0
        nominator = (set(wrk_tags)).intersection(set(i))
        denominator = (set(wrk_tags)).union(set(i))
        res = len(nominator)/len(denominator) #similarity

        if res > 0.10:
            jacard_sim.append(copy.deepcopy([wrk_id, sim_wrk_id, res]))
            tt += 1

    if tt >= 100:
        with open('./similar_works.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            for ii in jacard_sim:
                writer_object.writerow(ii)
            jacard_sim = []
            tt = 0  
            f_object.close()
            
            
if tt > 0:
    with open('./similar_works.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        for ii in jacard_sim:
            writer_object.writerow(ii)
        f_object.close()