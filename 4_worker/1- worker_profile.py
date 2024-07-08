import pandas as pd
import copy
from csv import writer

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")
users = pd.read_csv(r"../1_prepration/Users/Users.csv")
tags = pd.read_csv(r"../1_prepration/Tags/Tags.csv")

col = tags['TagName'].values.tolist()
col.insert(0, 'success_rate')
col.insert(0, 'reputation')
col.insert(0, 'user_id')

with open('./worker_info.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(col)
    f_object.close()

# users = users.loc[users['Id'].eq(171872).idxmax():]

workers_info = list()
for usr in users.iterrows():
    total_tag = []
    for i in range(len(tags['Id'])):
        total_tag.append(copy.deepcopy(int(0)))

    answers = posts.loc[(posts['OwnerUserId'] == usr[1]['Id']) & (posts['PostTypeId'] == 2)]
    answers_id = answers['Id'].values.tolist()
    rep =usr[1]['Reputation']

    if len(answers) == 0:
        continue

    val = answers['ParentId'].values.tolist()
    usr_qu = posts.loc[(posts['Id'].isin(val)) & (posts['PostTypeId'] == 1)]
    succ_ansrs = usr_qu.loc[usr_qu['AcceptedAnswerId'].isin(answers_id)]

    succ_rate = len(succ_ansrs) / len(answers)

    for qu in succ_ansrs.iterrows():

        if (str(qu[1]['Tags']) != 'nan'):
            qu_tag = qu[1]['Tags']
            qu_tag = qu_tag.replace('<', '')
            qu_tag = qu_tag.split('>')
            qu_tag.remove('')

        for tg in qu_tag:
            tag_id = tags.loc[tags['TagName'] == tg]
            if (tag_id.empty != True):
                index = int(tag_id.index[0])
                total_tag[index] += 1

    total_tag.insert(0, succ_rate)
    total_tag.insert(0, rep)
    total_tag.insert(0, usr[1]['Id'])

    with open('./worker_info.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(total_tag)
        f_object.close()

