import pandas as pd
import numpy as np
import copy
from csv import writer

work_prf = pd.read_csv(r"../3_work_profile/work_info.csv")

tt = 0
tags = list()
for wrk in work_prf.iterrows():
    wrkId = wrk[1]['Id']
    wrk = wrk[1].values.tolist()
    indeces = [i for i, e in enumerate(wrk) if e != 0]
    indeces.pop(0)
    indeces.insert(0, wrkId)
    tags.append(copy.deepcopy(indeces))
    tt += 1

    if tt == 100:
        with open('./indeces_of_tags.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            for ii in tags:
                writer_object.writerow(ii)
            tags = []  
            tt = 0
            f_object.close()

if tt > 0:
    with open('./indeces_of_tags.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        for ii in tags:
            writer_object.writerow(ii)
        tags = []  
        tt = 0
        f_object.close()