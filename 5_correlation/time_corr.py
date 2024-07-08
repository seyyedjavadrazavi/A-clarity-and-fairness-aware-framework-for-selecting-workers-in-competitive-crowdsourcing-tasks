import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import datetime
import copy
import time

def correlation():
    posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")

    answered_post = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]
    not_answered_post = posts.loc[(posts['PostTypeId'] == 1) & (posts['AcceptedAnswerId'].isnull())]

    AcAn_time = list()
    for question in answered_post.iterrows():
        answerPost = posts.loc[posts['Id'] == question[1]['AcceptedAnswerId']]

        element = datetime.datetime.strptime(question[1]['CreationDate'], "%Y-%m-%dT%H:%M:%S.%f")
        tuple = element.timetuple()
        questionCreationDate = time.mktime(tuple)

        answerTime = answerPost['CreationDate'].values

        element = datetime.datetime.strptime(answerTime[0], "%Y-%m-%dT%H:%M:%S.%f")
        tuple = element.timetuple()
        answerTime = time.mktime(tuple)
        AcAn_time.append(copy.deepcopy(answerTime - questionCreationDate))

    max_val = max(AcAn_time)

    not_AcAn_time = list()
    for i in range(len(not_answered_post['CreationDate'])):
        not_AcAn_time.append(copy.deepcopy(max_val + 1))

    time_dur = AcAn_time + not_AcAn_time

    AcAn_ones = [1] * len(AcAn_time)
    not_AcAn_zeros = [0] * len(not_AcAn_time)
    one_zeros = AcAn_ones + not_AcAn_zeros

    corr = np.corrcoef(one_zeros, time_dur)

    print("edit correlation = " + str(corr))

    corr, _ = spearmanr(one_zeros, time_dur)
    print('Spearmans correlation: %.3f' % corr)


correlation()