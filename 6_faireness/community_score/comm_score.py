##compare the community upvote score and requester's answer selection. 
import pandas as pd
import copy
import datetime

posts = pd.read_csv(r"../../1_prepration/Posts/Posts.csv")
users = pd.read_csv(r"../../1_prepration/Users/Users.csv")

questions = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]

unique_usrs = posts.OwnerUserId.unique()

compare = list()
for qu in questions.iterrows():
    answers = posts.loc[posts['ParentId'] == qu[1]['Id']]

    if len(answers) == 0:
        continue

    ac_an = answers.loc[answers['Id'] == qu[1]['AcceptedAnswerId']]

    if len(ac_an) == 0:
        continue

    ac_an_scr = ac_an['Score'].values[0]
    ac_an_time_stmp = ac_an['CreationDate'].values[0]
    ac_an_time_stmp = datetime.datetime.strptime(ac_an_time_stmp, "%Y-%m-%dT%H:%M:%S.%f")

    ac_An_id = qu[1]['AcceptedAnswerId']

    is_changed = -1
    for ans in answers.iterrows():
        ans_time_stmp = datetime.datetime.strptime(ans[1]['CreationDate'], "%Y-%m-%dT%H:%M:%S.%f")
        if (ac_an_scr < ans[1]['Score']):
            if (ac_an_time_stmp > ans_time_stmp):
                ac_An_id = ans[1]['Id']
                is_changed = 1

    compare.append(copy.deepcopy([qu[1]['Id'], qu[1]['OwnerUserId'], ac_An_id, ac_an_scr, is_changed]))

df_cols = ['quId', 'OwnerUserId', 'ac_an_id', 'ac_an_scr', 'is_changed']    
result = pd.DataFrame(compare, columns=df_cols) 
result.to_csv(r"./get_the_community_choise.csv", index = False, header=True)


collected_data = pd.read_csv(r"./get_the_community_choise.csv")
users_crowd_cmp = list()
for usr in unique_usrs:
    usr_res = collected_data.loc[collected_data['OwnerUserId'] == usr]
    usr_bad = usr_res.loc[usr_res['is_changed'] == 1] 
    if usr_res.empty == True:
        users_crowd_cmp.append(copy.deepcopy([usr, -1]))
    else:
        users_crowd_cmp.append(copy.deepcopy([usr, (len(usr_bad)/len(usr_res))]))

df_cols = ['UserId', 'changed_prcnt']
result = pd.DataFrame(users_crowd_cmp, columns=df_cols) 
result.to_csv(r"./usr_choise_result.csv", index = False, header=True)
