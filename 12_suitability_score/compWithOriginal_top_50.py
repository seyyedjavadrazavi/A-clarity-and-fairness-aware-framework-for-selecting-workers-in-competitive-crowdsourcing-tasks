import pandas as pd
import copy
import numpy as np
from csv import writer
from fuzzyFunc import fuzziModel

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")
test_data = pd.read_csv(r"../9_test_data/needed_testData_profiles_round_40_intersection_sim.csv")
ourself_golden_set = pd.read_csv(r"../11_ML/res_RobustScaler_scaler_jacard_v2_40.csv")
work_prf = pd.read_csv(r"../3_work_profile/work_info.csv")
worker_prf = pd.read_csv(r"../4_worker/indeces_of_non_zero_tags.csv", encoding="utf-8")
worker_prf_with_tags_name = pd.read_csv(r"../4_worker/worker_info.csv", encoding="utf-8")

ourself_golden_set = ourself_golden_set.loc[ourself_golden_set['label'] == 1]
uniq_test_data = test_data.drop_duplicates(subset=['workId'])

cnter = 0
cnt = 0
res = list()

with open('20_top_person_all_wrkrs_not_1_new.csv', 'w', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(['workId', 'userId', 'similarity'])
    f_object.close()

with open('50_top_person_all_wrkrs_not_1_new.csv', 'w', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(['workId', 'userId', 'similarity'])
    f_object.close()

for test in uniq_test_data.iterrows():
    ansr = posts.loc[posts['Id'] == test[1]['workId'], 'AcceptedAnswerId'].values[0]
    orgnlWrkr = posts.loc[posts['Id'] == ansr, 'OwnerUserId']

    is_nan = np.isnan(np.min(orgnlWrkr.values))
    if is_nan == True:
        continue
    else:
        orgnlWrkr = orgnlWrkr.values[0]

    wrk = work_prf.loc[work_prf['Id'] == test[1]['workId']]

    if wrk.empty == True:
        continue

    wrk_values = wrk.values[0].tolist()
    wrkId = wrk_values[0]
    wrk_tags = wrk_values[1:]
    wrk_tags = [i for i, e in enumerate(wrk_tags) if e != 0]
    cols = wrk.columns.values.tolist()
    tags = list()
    for i in wrk_tags:
        tags.append(copy.deepcopy(cols[i+1]))
    
    wrk_tags = []
    wrk_tags = tags

    candidates = pd.DataFrame()
    cand = ourself_golden_set.loc[(ourself_golden_set['workId'] == test[1]['workId'])]
    if len(cand) == 0:
        cnt += 1
        continue
    else:
        candidates = pd.concat([candidates, cand], ignore_index=True)

    candidates = candidates.sort_values(by='wrkr_qu_sim', ascending=False)
    candidates = candidates.drop_duplicates(subset=['workerId'])
    candidates = candidates['workerId'].values.tolist()
    candidates = candidates[:50]

    orgId = int(orgnlWrkr)

    orgWrkr = worker_prf.loc[worker_prf['workerId'] == orgnlWrkr]        
    if orgWrkr.empty == True:
        continue
    orgWrkr = orgWrkr.values[0].tolist()
    orgWrkr_rep = orgWrkr[1]
    orgWrkr_tags = orgWrkr[3:]
    orgWrkr_tags = np.array(orgWrkr_tags)
    orgWrkr_tags = (orgWrkr_tags[np.logical_not(np.isnan(orgWrkr_tags))]).tolist()

    tags = []
    for i in orgWrkr_tags:
        tags.append(copy.deepcopy(cols[int(i)-2]))
    orgWrkr_tags = []
    orgWrkr_tags = tags 
    
    orgWrkr_qu_tags = []
    orgWrkr_qu_tags = list(set.intersection(set(wrk_tags), set(orgWrkr_tags)))
    orgWrkr_qu_tags_val = worker_prf_with_tags_name.loc[worker_prf_with_tags_name['user_id'] == orgnlWrkr, orgWrkr_qu_tags]

    for usr in candidates:
        # print(usr)
        simWrkr = worker_prf.loc[worker_prf['workerId'] == int(usr)]
        if simWrkr.empty == True:
            continue
        simWrkr = simWrkr.values[0].tolist()
        simWrkr_rep = simWrkr[1]
        simWrkr_tags = simWrkr[3:]

        simWrkr_tags = np.array(simWrkr_tags)
        simWrkr_tags = (simWrkr_tags[np.logical_not(np.isnan(simWrkr_tags))]).tolist()
        tags = []
    
        for i in simWrkr_tags:
            tags.append(copy.deepcopy(cols[int(i)-2]))
    
        simWrkr_tags = []
        simWrkr_tags = tags
    
        simwrkr_qu_tgs = []
        simwrkr_qu_tgs = set.intersection(set(wrk_tags), set(simWrkr_tags))

        simwrkr_orgnlWrkr_qu_tgs = list(set.intersection(set(orgWrkr_qu_tags), set(simwrkr_qu_tgs)))
        simwrkr_qu_tags_val = worker_prf_with_tags_name.loc[worker_prf_with_tags_name['user_id'] == int(usr), simwrkr_orgnlWrkr_qu_tgs]
        
        indices = [i for i, x in enumerate(orgWrkr_qu_tags) if x in simwrkr_orgnlWrkr_qu_tgs]

        orgWrkr_qu_tags_val_list = orgWrkr_qu_tags_val.values[0].tolist()
        simwrkr_qu_tags_val = simwrkr_qu_tags_val.values[0].tolist()
        
        orgWrkr_qu_tags_val_list = [orgWrkr_qu_tags_val_list[i] for i in indices]

        tgs_res = [i / j for i, j in zip(simwrkr_qu_tags_val, orgWrkr_qu_tags_val_list)]

        for x in range(len(tgs_res)):
            if tgs_res[x] > 1:
                tgs_res[x] = 1 
        
        if len(tgs_res) == 0:
            continue
        
        tgs_avg = sum(tgs_res)/len(tgs_res)
        fuzz_res = []
        fuzz_res = fuzziModel(orgWrkr_rep, 1, simWrkr_rep, tgs_avg)
        
        res.append([test[1]['workId'], usr, fuzz_res])
        
        # res = pd.DataFrame(res, columns=['workId', 'userId', 'wrkr_qu_sim'])
        # res.sort_values('wrkr_qu_sim')
        # res = res[:50].values.tolist()
        
    with open('50_top_person_all_wrkrs_not_1_new.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        for ii in res:
            writer_object.writerow(ii)
        f_object.close()

    with open('20_top_person_all_wrkrs_not_1_new.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        res = res[:20]
        for ii in res:
            writer_object.writerow(ii)
        f_object.close()
    
    res = []  

print(cnt)
# file1 = open("compare_last_top_50.txt","w")
# file1.write("/n")
# file1.write(str(originals))
# file1.write("/n")
# file1.write(str(originals/cnter))
# file1.write("/n")
# file1.write(str(moreThan_40))