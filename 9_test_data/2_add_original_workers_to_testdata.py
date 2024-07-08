import pandas as pd
import copy
from csv import writer
import numpy as np

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")
req_clarity = pd.read_csv(r"../7_clarity/fuzzy model/res2.csv")
req_fairness_candidate = pd.read_csv(r"../6_faireness/candidate/candidate_result.csv")
req_fairness_comm_scr = pd.read_csv(r"../6_faireness/community_score/usr_choise_result.csv")
req_prf = pd.read_csv(r"../2_requester_profile/requesters_non_zero_tags.csv")
worker_prf = pd.read_csv(r"../4_worker/indeces_of_non_zero_tags.csv", encoding="utf-8")
work_prf = pd.read_csv(r"../8_similar_works/indeces_of_tags.csv")
similar_works = pd.read_csv(r"./needed_testData_profiles_round_40_intersection_sim.csv")

similar_works = similar_works.drop_duplicates()
questions = similar_works.drop_duplicates(subset=['workId'])

cnt = 0
infos = list()
isFirst = False
creq = 0

for qu in questions.iterrows():
    profile = list()
    
    curr_qu = posts.loc[posts['Id'] == qu[1]['workId']]
    
    if curr_qu.empty == True:
        continue

    req_prf_cl = req_clarity.loc[req_clarity['QuestionId'] == curr_qu['OwnerUserId'].values[0]]
    if req_prf_cl.empty == True:
        continue
    else:
        req_prf_cl = req_prf_cl.values[0][1]
    
    req_frn_cand = req_fairness_candidate.loc[req_fairness_candidate['UserId'] == curr_qu['OwnerUserId'].values[0]]
    if req_frn_cand.empty == True:
        continue
    else:
        req_frn_cand = req_frn_cand['percentage'].values[0]

    req_frn_com = req_fairness_comm_scr.loc[req_fairness_comm_scr['UserId'] == curr_qu['OwnerUserId'].values[0]]
    req_frn_com = req_frn_com['changed_prcnt'].values[0]

    req_prf_exp = req_prf.loc[req_prf['requesterId'] == curr_qu['OwnerUserId'].values[0]]
    
    if req_prf_exp.empty == True:
        creq += 1
        continue

    req_rep = req_prf_exp['reputation'].values[0]
    req_success_rate = req_prf_exp['success_rate'].values[0]
    
    ######################## question
    qu_prf = work_prf.loc[work_prf['question_id'] == qu[1]['workId']]
    if qu_prf.empty == True:
        continue

    wrk_tags = qu_prf.iloc[:, 1:]
    wrk_tags = np.array(wrk_tags.values[0].tolist())
    wrk_tags_val = (wrk_tags[np.logical_not(np.isnan(wrk_tags))]).tolist()

    answers = posts.loc[posts['ParentId'] == qu[1]['workId']]
    ###################### workers 
    for ansr in answers.iterrows():
        profile = []    
        curr_ans = ansr[1]

        wrkr = worker_prf.loc[worker_prf['workerId'] == ansr[1]['OwnerUserId']]
        if len(wrkr) < 1:
            continue
            
        wrkr = wrkr.values[0].tolist()
        wrkrId = wrkr[0]
        wrkr_rep = wrkr[1]
        wrkr_success_rate = wrkr[2]

        wrkr_tags = wrkr[3:]
        
        if (len(wrk_tags_val) == 0) | (len(wrkr_tags ) == 0):
            continue

        wrkr_tags = np.array(wrkr_tags)
        wrkr_tags = (wrkr_tags[np.logical_not(np.isnan(wrkr_tags))]).tolist()

        wrkr_qu_sim = 0
        i=set.intersection(set(wrk_tags_val), set(wrkr_tags))
        nominator = (set(wrk_tags_val)).intersection(set(i))
        denominator = (set(wrk_tags_val)).union(set(i))
        wrkr_qu_sim = len(nominator)/len(denominator) #similarity

        qu_qu_sim = 1

        label = 1
        try:
            profile.append(copy.deepcopy(qu[1]['workId']))
            profile.append(copy.deepcopy(ansr[1]['Id']))
            profile.append(copy.deepcopy(curr_qu['OwnerUserId'].values[0]))
            profile.append(copy.deepcopy(curr_ans['OwnerUserId']))
            
            profile.append(copy.deepcopy(wrkr_rep)) 
            profile.append(copy.deepcopy(wrkr_success_rate)) 
            profile.append(copy.deepcopy(wrkr_qu_sim))
            profile.append(copy.deepcopy(qu_qu_sim))
            profile.append(copy.deepcopy(req_prf_cl))
            profile.append(copy.deepcopy(req_frn_cand))

            profile.append(copy.deepcopy(req_frn_com))
            profile.append(copy.deepcopy(req_rep))
            profile.append(copy.deepcopy(req_success_rate))
            profile.append(copy.deepcopy(0))
            profile.append(copy.deepcopy(label))
        except:
            a = -1

        infos.append(copy.deepcopy(profile))

        with open('needed_testData_profiles_round_40_intersection_sim.csv', 'a', newline='') as f_object:  
            writer_object = writer(f_object)
            for ii in infos:
                writer_object.writerow(ii)
            infos = []  
            f_object.close()