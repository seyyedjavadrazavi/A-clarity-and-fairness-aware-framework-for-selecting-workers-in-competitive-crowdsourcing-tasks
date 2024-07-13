import pandas as pd
import math
import copy
from concurrent.futures import ThreadPoolExecutor, as_completed

Posts = pd.read_csv('../../1_prepration/Posts/Posts.csv', encoding='utf-8')
test_data = pd.read_csv("../../9_test_data/needed_testData_profiles_round_40_intersection_sim.csv")
sharif_golden_set = pd.read_csv('../paper_1_res/sharif/1_cmb_res.csv', encoding='utf-8')
china_golden_set = pd.read_csv('../paper_1_res/china/experts.csv', encoding='utf-8')
our_golden_set = pd.read_csv('../../12_suitability_score/50_top_person_all_wrkrs_not_1_new.csv', encoding='utf-8')  

workIds = test_data.drop_duplicates(subset=['workId'])
workIds = workIds['workId'].values.tolist()

def calculate_rbp(id, p=0.9):

    wrks = Posts.loc[(Posts['Id'] == id) & (Posts['PostTypeId'] == 1)]
    if wrks.empty == True:
        return 0
    
    ##### tags
    tags = wrks['Tags'].values[0]
    tags = tags.split('<')
    tags = {x.replace('>', '') for x in tags}
    tags.remove('')

    ######## org wrkr
    acan_ids = wrks['AcceptedAnswerId'].values.tolist()    
    answrs = Posts.loc[(Posts['Id'].isin(acan_ids)) & (Posts['PostTypeId'] == 2)]
    org_wrkr = answrs['OwnerUserId'].values[0]

    ####### slct similar wrkrs
    wrkr_no_in_each_tg = 50

    shrf_sim_wrkrs= []
    chna_sim_wrkrs= []
    for tg in tags:
        shrf_gldn_wrkrs = sharif_golden_set.loc[sharif_golden_set['tag'] == tg]
        shrf_gldn_wrkrs.sort_values(['score'], inplace=True, ascending=False)
        shrf_sim_wrkrs.extend(shrf_gldn_wrkrs['userId'].values.tolist()[:wrkr_no_in_each_tg])

        chna_gldn_wrkrs = china_golden_set.loc[china_golden_set['tagName'] == tg]    
        chna_gldn_wrkrs.sort_values(['score'], inplace=True, ascending=False)
        chna_sim_wrkrs.extend(chna_gldn_wrkrs['workerId'].values.tolist()[:wrkr_no_in_each_tg])     

    our_wrkrs = our_golden_set.loc[our_golden_set['workId'] == id]
    our_wrkrs.sort_values(['similarity'], inplace=True, ascending=False)
    our_sim_wrkrs = our_wrkrs['userId'].values.tolist()[:wrkr_no_in_each_tg]

    if len(shrf_sim_wrkrs) == 0 or len(chna_sim_wrkrs) == 0 or len(our_sim_wrkrs) == 0:
        return 0

    try:
        ########## rbp  
        if org_wrkr in shrf_sim_wrkrs:  
            shrf_rank = shrf_sim_wrkrs.index(org_wrkr) + 1
            shrf_rbp = (p**(shrf_rank + 1)) * (1 - p)
        else:
            shrf_rbp = 0

        if org_wrkr in chna_sim_wrkrs:  
            chna_rank = chna_sim_wrkrs.index(org_wrkr) + 1
            chna_rbp = (p**(chna_rank + 1)) * (1 - p)
        else:
            chna_rbp = 0

        if org_wrkr in our_sim_wrkrs:  
            our_rank = our_sim_wrkrs.index(org_wrkr) + 1
            our_rbp = (p**(our_rank + 1)) * (1 - p)
        else:
            our_rbp = 0

        ########## DCG  
        if org_wrkr in shrf_sim_wrkrs:  
            shrf_rank = shrf_sim_wrkrs.index(org_wrkr) + 1
            shrf_dcg = (1 / math.log2(shrf_rank+2)) 
        else:
            shrf_dcg = 0

        if org_wrkr in chna_sim_wrkrs:  
            chna_rank = chna_sim_wrkrs.index(org_wrkr) + 1
            chna_dcg = (1 / math.log2(chna_rank+2)) 
        else:
            chna_dcg = 0

        if org_wrkr in our_sim_wrkrs:  
            our_rank = our_sim_wrkrs.index(org_wrkr) + 1
            our_dcg = (1 / math.log2(our_rank+2)) 
        else:
            our_dcg = 0
            
        ########## MAP  
        if org_wrkr in shrf_sim_wrkrs:
            shrf_rank = shrf_sim_wrkrs.index(org_wrkr) + 1
            shrf_map = 1/ shrf_rank 
        else:
            shrf_map = 0

        if org_wrkr in chna_sim_wrkrs:  
            chna_rank = chna_sim_wrkrs.index(org_wrkr) + 1
            chna_map = 1 / chna_rank 
        else:
            chna_map = 0

        if org_wrkr in our_sim_wrkrs:  
            our_rank = our_sim_wrkrs.index(org_wrkr) + 1
            our_map = 1 / our_rank 
        else:
            our_map = 0

        # ########## MRR 
        if org_wrkr in shrf_sim_wrkrs:
            shrf_rank = shrf_sim_wrkrs.index(org_wrkr) + 1
            shrf_mrr = 1 / shrf_rank 
        else:
            shrf_mrr = 0

        if org_wrkr in chna_sim_wrkrs:  
            chna_rank = chna_sim_wrkrs.index(org_wrkr) + 1
            chna_mrr = 1 / chna_rank 
        else:
            chna_mrr = 0

        if org_wrkr in our_sim_wrkrs:  
            our_rank = our_sim_wrkrs.index(org_wrkr) + 1
            our_mrr = 1 / our_rank 
        else:
            our_mrr = 0
        
        ########## P@K
        if org_wrkr in shrf_sim_wrkrs:
            shrf_p_at_k = 1 / len(shrf_sim_wrkrs)
        else:
            shrf_p_at_k = 0

        if org_wrkr in chna_sim_wrkrs:  
            chna_p_at_k = 1 / len(chna_sim_wrkrs)
        else:
            chna_p_at_k = 0

        if org_wrkr in our_sim_wrkrs:  
            our_p_at_k = 1 / len(our_sim_wrkrs)
        else:
            our_p_at_k = 0
         
    except ValueError:
        print(ValueError)

    rr = [id, shrf_rbp, chna_rbp, our_rbp, shrf_dcg, chna_dcg, our_dcg, shrf_map, chna_map, our_map,
                shrf_mrr, chna_mrr, our_mrr, shrf_p_at_k, chna_p_at_k, our_p_at_k]
    return rr

if __name__ == '__main__':
    shrf_rbp_lst = []
    chna_rbp_lst = [] 
    our_rbp_lst = []
    
    shrf_dcg_lst = []
    chna_dcg_lst = [] 
    our_dcg_lst = []

    shrf_map_lst = []
    chna_map_lst = [] 
    our_map_lst = []    

    shrf_mrr_lst = []
    chna_mrr_lst = [] 
    our_mrr_lst = []

    shrf_p_at_k_lst = []
    chna_p_at_k_lst = [] 
    our_p_at_k_lst = []

    idcg = 1

    res = calculate_rbp(workIds[0])
    xxx = calculate_rbp(workIds[1])
    xxx = calculate_rbp(workIds[2])
    workIds = workIds[:10]
    with ThreadPoolExecutor(max_workers=15) as executor:
        
        futures = [executor.submit(calculate_rbp, wid)  
                   for wid in workIds]
        
    for wrk in workIds:
        res = calculate_rbp(wrk) 
        if res == 0:
            continue
        
        wrkId = res[0]

        shrf_p_at_k_lst.append(res[1])
        chna_p_at_k_lst.append(res[2])
        our_p_at_k_lst.append(res[3])

        shrf_map_lst.append(res[4])
        chna_map_lst.append(res[5])
        our_map_lst.append(res[6])

        shrf_rbp_lst.append(res[0+1])
        chna_rbp_lst.append(res[1+1])
        our_rbp_lst.append(res[2+1])
            
        shrf_dcg_lst.append(res[3+1])
        chna_dcg_lst.append(res[4+1])
        our_dcg_lst.append(res[5+1])

        shrf_map_lst.append(res[6+1])
        chna_map_lst.append(res[7+1])
        our_map_lst.append(res[8+1])

        shrf_mrr_lst.append(res[9+1])
        chna_mrr_lst.append(res[10+1])
        our_mrr_lst.append(res[11+1])

        shrf_p_at_k_lst.append(res[12+1])
        chna_p_at_k_lst.append(res[13+1])
        our_p_at_k_lst.append(res[14+1])

    # Calculate averages
    shrf_rbp = sum(shrf_rbp_lst) / len(shrf_rbp_lst) 
    chna_rbp = sum(chna_rbp_lst) / len(chna_rbp_lst)
    our_rbp = sum(our_rbp_lst) / len(our_rbp_lst)
    
    # Calculate averages
    shrf_dcg = sum(shrf_dcg_lst) / len(shrf_dcg_lst) 
    chna_dcg = sum(chna_dcg_lst) / len(chna_dcg_lst)
    our_dcg = sum(our_dcg_lst) / len(our_dcg_lst)

    # Calculate averages
    shrf_map = sum(shrf_map_lst) / len(shrf_map_lst) 
    chna_map = sum(chna_map_lst) / len(chna_map_lst)
    our_map = sum(our_map_lst) / len(our_map_lst)    


    # Calculate averages
    shrf_mrr = sum(shrf_mrr_lst) / len(shrf_mrr_lst) 
    chna_mrr = sum(chna_mrr_lst) / len(chna_mrr_lst)
    our_mrr = sum(our_mrr_lst) / len(our_mrr_lst)

    # Calculate averages
    shrf_p_at_k = sum(shrf_p_at_k_lst) / len(shrf_p_at_k_lst) 
    chna_p_at_k = sum(chna_p_at_k_lst) / len(chna_p_at_k_lst)
    our_p_at_k = sum(our_p_at_k_lst) / len(our_p_at_k_lst)


    print("Results rbp:")
    print(shrf_rbp)
    print(chna_rbp) 
    print(our_rbp)

    print("Results dcg:")
    print(shrf_dcg)
    print(chna_dcg) 
    print(our_dcg)    

    print("Results mrr:")
    print(shrf_mrr)
    print(chna_mrr) 
    print(our_mrr)

    print("Results p at k:")
    print(shrf_p_at_k)
    print(chna_p_at_k) 
    print(our_p_at_k)

    print("Results map:")
    print(shrf_map)
    print(chna_map) 
    print(our_map)


    wrkId = [int(wrkId)] * len(shrf_rbp_lst)

    shrf_df = pd.DataFrame(columns=['wrkId', 'rbp_score', 'dcg_score', 'map_score', 'mrr_score', 'p_at_k_score'])
    shrf_df['wrkId'] = wrkId
    shrf_df['rbp_score'] = shrf_rbp_lst 
    shrf_df['dcg_score'] = shrf_dcg_lst
    shrf_df['map_score'] = shrf_map_lst
    shrf_df['mrr_score'] = shrf_mrr_lst
    shrf_df['p_at_k_score'] = shrf_p_at_k_lst
    shrf_df.to_csv(r"./sharif_top_10.csv", index = False, header=True)

    chna_df = pd.DataFrame(columns=['wrkId', 'rbp_score', 'dcg_score', 'map_score', 'mrr_score', 'p_at_k_score'])
    chna_df['wrkId'] = wrkId
    chna_df['rbp_score'] = chna_rbp_lst 
    chna_df['dcg_score'] = chna_dcg_lst
    chna_df['map_score'] = chna_map_lst
    chna_df['mrr_score'] = chna_mrr_lst
    chna_df['p_at_k_score'] = chna_p_at_k_lst    
    chna_df.to_csv(r"./china_top_10.csv", index = False, header=True)

    our_df = pd.DataFrame(columns=['wrkId', 'rbp_score', 'dcg_score', 'map_score', 'mrr_score', 'p_at_k_score'])
    our_df['wrkId'] = wrkId
    our_df['rbp_score'] = our_rbp_lst 
    our_df['dcg_score'] = our_dcg_lst
    our_df['map_score'] = our_map_lst
    our_df['mrr_score'] = our_mrr_lst
    our_df['p_at_k_score'] = our_p_at_k_lst    
    our_df.to_csv(r"./our_top_10.csv", index = False, header=True)
    
    