import pandas as pd
import copy
import numpy as np
from csv import writer

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")
req_clarity = pd.read_csv(r"../7_clarity/fuzzy model/res2.csv")
req_fairness_candidate = pd.read_csv(r"../6_faireness/candidate/candidate_result.csv")
req_fairness_comm_scr = pd.read_csv(r"../6_faireness/community_score/usr_choise_result.csv")
req_prf = pd.read_csv(r"../2_requester_profile/requesters_non_zero_tags.csv")
worker_prf = pd.read_csv(r"../4_worker/indeces_of_non_zero_tags.csv")
work_prf = pd.read_csv(r"../8_similar_works/indeces_of_tags.csv")

questions = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]

cnt = 0
infos = list()
isFirst = True
tt = 0
for qu in questions.iterrows():
    profile = list()
    
    req_prf_cl = req_clarity.loc[req_clarity['QuestionId'] == qu[1]['OwnerUserId']]
    if req_prf_cl.empty == True:
        continue
    else:
        req_prf_cl = req_prf_cl.values[0][1]
    
    req_frn_cand = req_fairness_candidate.loc[req_fairness_candidate['UserId'] == qu[1]['OwnerUserId']]
    if req_frn_cand.empty == True:
        continue
    else:
        req_frn_cand = req_frn_cand['percentage'].values[0]

    req_frn_com = req_fairness_comm_scr.loc[req_fairness_comm_scr['UserId'] == qu[1]['OwnerUserId']]
    req_frn_com = req_frn_com['changed_prcnt'].values[0]

    req_prf_exp = req_prf.loc[req_prf['requesterId'] == qu[1]['OwnerUserId']]
    
    req_rep = req_prf_exp['reputation'].values[0]
    req_success_rate = req_prf_exp['success_rate'].values[0]
    
    ####################### question
    qu_prf = work_prf.loc[work_prf['question_id'] == qu[1]['Id']]
    if qu_prf.empty == True:
        continue

    wrk_tags = qu_prf.iloc[:, 1:]
    wrk_tags = np.array(wrk_tags.values[0].tolist())
    wrk_tags_val = (wrk_tags[np.logical_not(np.isnan(wrk_tags))]).tolist()

    ###################### workers 
    ansrs = posts.loc[posts['ParentId'] == qu[1]['Id']]
    for ans in ansrs.iterrows():
        profile = []

        wrkr = worker_prf.loc[worker_prf['workerId'] == ans[1]['OwnerUserId']]
        if len(wrkr) < 1:
            continue
        
        # wrkrId = wrkr[1]
        wrkr_rep = wrkr['reputation'].values[0]
        wrkr_success_rate = wrkr['success_rate'].values[0]

        wrkr_tags = wrkr.values[0][3:]
        
        if (len(wrk_tags_val) == 0) | (len(wrkr_tags ) == 0):
            continue

        wrkr_tags = np.array(wrkr_tags)
        wrkr_tags = (wrkr_tags[np.logical_not(np.isnan(wrkr_tags))]).tolist()

        i = set.intersection(set(wrk_tags_val),set(wrkr_tags))

        wrkr_qu_sim = 0
        nominator = (set(wrk_tags_val)).intersection(set(i))
        denominator = (set(wrk_tags_val)).union(set(i))

        wrkr_qu_sim = len(nominator)/len(denominator) #similarity

        if wrkr_qu_sim < 0.15:
            continue

        if ans[1]['Id'] == qu[1]['AcceptedAnswerId']:
            label = 1
        else:
            label = 0

        try:
            profile.append(copy.deepcopy(qu[1]['Id']))
            profile.append(copy.deepcopy(qu[1]['OwnerUserId']))
            profile.append(copy.deepcopy(ans[1]['OwnerUserId']))
            
            profile.append(copy.deepcopy(wrkr_rep)) 
            profile.append(copy.deepcopy(wrkr_success_rate)) 
            profile.append(copy.deepcopy(wrkr_qu_sim))

            profile.append(copy.deepcopy(req_prf_cl))
            profile.append(copy.deepcopy(req_frn_cand))
            profile.append(copy.deepcopy(req_frn_com))
            profile.append(copy.deepcopy(req_rep))
            profile.append(copy.deepcopy(req_success_rate))

            profile.append(copy.deepcopy(label))

            cnt += 1
        except:
            print(cnt)

        infos.append(copy.deepcopy(profile))
        tt += 1 

        if tt == 100:
            if isFirst == True:
                with open('combination_of_profiles_similarities.csv', 'a', newline='') as f_object:  
                    writer_object = writer(f_object)
                    df_cols = ['workId', 'requesterId', 'workerId', 'wrkr_rep', 'wrkr_success_rate', 'wrkr_qu_sim',
                   'req_prf_cl', 'req_frn_cand', 'req_frn_com', 'req_rep', 'req_success_rate', 'label']
                    writer_object.writerow(df_cols)
                    for ii in infos:
                        writer_object.writerow(ii)
                    infos = []  
                    f_object.close()
                    tt = 0
                isFirst = False
            else:
                with open('combination_of_profiles_similarities.csv', 'a', newline='') as f_object:  
                    writer_object = writer(f_object)
                    for ii in infos:
                        writer_object.writerow(ii)
                    infos = []  
                    f_object.close()
                    tt = 0

if tt > 0:
    with open('combination_of_profiles_similarities.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        for ii in infos:
            writer_object.writerow(ii)
        f_object.close()