import pandas as pd
import numpy as np
import time
import datetime
import copy
from fuzzyFunc import fuzziModel
# from sigmoid import sigmoidFunc
import statistics
from csv import writer

posts = pd.read_csv("../../1_prepration/Posts/Posts.csv")
users = pd.read_csv("../../1_prepration/Users/Users.csv")
postsHistory = pd.read_csv("../../1_prepration/postHistory/postsHistory.csv")

questions = posts.loc[(posts['PostTypeId'] == 1)]

with open('./res.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(['QuestionId', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'fuzzi_score'])
    f_object.close()
    
with open('./res2.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(['QuestionId', 'fuzzi_score'])
    f_object.close()

# counter = 0

standard_time = list()

Reputation_sd = statistics.pstdev(users['Reputation'])
print("Reputation standard devition :" + str(Reputation_sd))
print("Reputation median: " + str(statistics.median(users['Reputation'])))
Reputation_mean = sum(users['Reputation']) / len(users['Reputation'])
print("Reputation mean: " + str(Reputation_mean))


# users = users.loc[users['Id'] > 1499122]
for usr in users.iterrows():
    # if counter == 73:
    #     a = "bad time bit map"
    # print(counter)
    
    succ_ques_rtio = 0
    rep = 0
    cmmnts_ques_rtio = 0
    edit_rtio = 0
    # number0 = Success rate
    # number1 = Reputation
    # number2 = Comment ratio
    # number3 = Edit ratio
    a = 0

    usr_ques = posts.loc[posts['OwnerUserId'] == usr[1]['Id']]
    
    if len(usr_ques) == 0:
            continue

    succ_ques = usr_ques.loc[~usr_ques['AcceptedAnswerId'].isnull()]
    cmmnts_ques = usr_ques.loc[usr_ques['CommentCount'] != 0]
    answerPost = usr_ques.loc[~usr_ques['LastEditDate'].isnull()]

    succ_ques_rtio = len(succ_ques) / len(usr_ques) 
    rep = usr[1]['Reputation']
    if rep > 1600:
         rep = 1600

    rep = rep / 1600

    cmmnts_ques_rtio = len(cmmnts_ques) / len(usr_ques)
    edit_rtio = len(answerPost) / len(usr_ques)

    try :
        fz_res = fuzziModel(succ_ques_rtio, rep, cmmnts_ques_rtio, edit_rtio)
    except:
        print('exccept' + str(usr[1]['Id']))
        continue

    with open('./res.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow([usr[1]['Id'], succ_ques_rtio, rep, cmmnts_ques_rtio, edit_rtio , fz_res])
        f_object.close()
    
    with open('./res2.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow([usr[1]['Id'], fz_res])
        f_object.close()

