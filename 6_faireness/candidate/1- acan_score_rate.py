import pandas as pd
import copy

posts = pd.read_csv(r"../../1_prepration/Posts/Posts.csv")
users = pd.read_csv(r"../../1_prepration/Users/Users.csv")

questions = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]

unique_usrs = posts.OwnerUserId.unique()

score_list = list()
for usr in users.iterrows():
    qu = questions.loc[questions['OwnerUserId'] == usr[1]['Id']]
    if qu.empty == True:
        continue
    
    res = pd.merge(qu, posts, how='inner', left_on='AcceptedAnswerId', right_on='Id')
    usr_scrs = list()
    for i in res.iterrows():
        scr = i[1]['Score_y']
        usr_scrs.append(copy.deepcopy(scr))

    if len(usr_scrs) == 0:
        score_list.append(copy.deepcopy([usr[1]['Id'], 0]))
    else:
        score_list.append(copy.deepcopy([usr[1]['Id'], sum(usr_scrs)/len(usr_scrs)]))

df_cols = ['UserId', 'avg_scores']
result = pd.DataFrame(score_list, columns=df_cols) 
result.to_csv(r"./  .csv", index = False, header=True)