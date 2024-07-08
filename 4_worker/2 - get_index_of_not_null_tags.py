import pandas as pd
import copy
from csv import writer

work_prf = pd.read_csv(r"./worker_info.csv")

tt = 0
isFirst = True
tags = list()
for wrk in work_prf.iterrows():
    wrkerId = wrk[1]['user_id']
    rep = wrk[1]['reputation']
    succ_rate = wrk[1]['success_rate']
    wrk = wrk[1].values.tolist()
    indeces = [i for i, e in enumerate(wrk) if e != 0]
    if len(indeces) < 3:
        continue
    indeces.pop(0)
    indeces.pop(0)
    indeces.pop(0)
    indeces.insert(0, wrkerId)
    indeces.insert(1, rep)
    indeces.insert(2, succ_rate)
    tags.append(copy.deepcopy(indeces))
    tt += 1

    if tt == 100:
        if isFirst == True:
            cols = ['tag' + str(i) for i in range(1, 616)]
            cols.insert(0, 'workerId')
            cols.insert(1, 'reputation')
            cols.insert(2, 'success_rate')
            with open('./indeces_of_non_zero_tags.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(cols)
                for ii in tags:
                    writer_object.writerow(ii)
                tags = []  
                tt = 0
                isFirst = False
                f_object.close()
        else:
            with open('./indeces_of_non_zero_tags.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                for ii in tags:
                    writer_object.writerow(ii)
                tags = []  
                tt = 0
                f_object.close()

if tt > 0:
    with open('./indeces_of_non_zero_tags.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        for ii in tags:
            writer_object.writerow(ii)
        tags = []  
        tt = 0
        f_object.close()