import pandas as pd
import copy
from csv import writer

requester_prf = pd.read_csv(r"requester_profile.csv")

tt = 0
isFirst = True
tags = list()
for req in requester_prf.iterrows():
    reqId = req[1]['UserId']
    rep = req[1]['Reputation']
    succ_rate = req[1]['Succcess_rate']
    req = req[1].values.tolist()
    indeces = [i for i, e in enumerate(req) if e != 0]
    if len(indeces) < 3:
        continue
    indeces.pop(0)
    indeces.pop(0)
    indeces.pop(0)
    indeces.insert(0, reqId)
    indeces.insert(1, rep)
    indeces.insert(2, succ_rate)
    tags.append(copy.deepcopy(indeces))
    tt += 1

    if tt == 100:
        if isFirst == True:
            cols = ['tag' + str(i) for i in range(1, 143)]
            cols.insert(0, 'requesterId')
            cols.insert(1, 'reputation')
            cols.insert(2, 'success_rate')
            with open('requesters_non_zero_tags.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(cols)
                for ii in tags:
                    writer_object.writerow(ii)
                tags = []  
                tt = 0
                isFirst = False
                f_object.close()
        else:
            with open('requesters_non_zero_tags.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                for ii in tags:
                    writer_object.writerow(ii)
                tags = []  
                tt = 0
                f_object.close()

if tt > 0:
    with open('requesters_non_zero_tags.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        for ii in tags:
            writer_object.writerow(ii)
        tags = []  
        tt = 0
        f_object.close()