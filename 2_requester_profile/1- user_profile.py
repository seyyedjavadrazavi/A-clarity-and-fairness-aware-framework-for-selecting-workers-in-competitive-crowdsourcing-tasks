import pandas as pd
import copy
from csv import writer

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")
tags = pd.read_csv(r"../1_prepration/Tags/Tags.csv")
users = pd.read_csv(r"../1_prepration/Users/Users.csv")

new_columns = list()
new_columns.append(copy.deepcopy('UserId'))
new_columns.append(copy.deepcopy('Reputation'))
new_columns.append(copy.deepcopy('Succcess_rate'))
new_columns.extend(tags['TagName'].values.tolist())

with open('requester_profile.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(new_columns)
    f_object.close()

for user in users.iterrows():
    success_tag = list()

    rep = user[1]['Reputation']
    succ_rate = 0

    user_questions = posts.loc[(posts['OwnerUserId'] == user[1]['Id']) & (posts['PostTypeId'] == 1)]
    if user_questions.empty:
        continue

    user_succ_ques = user_questions.loc[~user_questions['AcceptedAnswerId'].isnull()]
    succ_rate = len(user_succ_ques) / len(user_questions)

    for i in range(len(tags['Id'])):
        success_tag.append(copy.deepcopy(int(0)))

    for question in user_succ_ques.iterrows():
        if (str(question[1]['Tags']) != 'nan'):
            qu_tag = question[1]['Tags']
            qu_tag = qu_tag.replace('<', '')
            qu_tag = qu_tag.split('>')
            qu_tag.remove('')
            for tg in qu_tag:
                tag_id = tags.loc[tags['TagName'] == tg]
                if (tag_id.empty != True) & (str(question[1]['AcceptedAnswerId']) != 'nan'):
                    index = int(tag_id.index[0]) 
                    success_tag[index] += 1
    
    success_tag.insert(0, succ_rate)
    success_tag.insert(0, rep)
    success_tag.insert(0, user[1]['Id'])

    with open('requester_profile.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(success_tag)
        f_object.close()
