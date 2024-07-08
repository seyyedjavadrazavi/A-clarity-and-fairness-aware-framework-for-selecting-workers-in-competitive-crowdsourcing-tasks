import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import datetime
import copy
import time

def correlation():
    posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")
    postsHistory = pd.read_csv("../1_prepration/postHistory/postsHistory.csv")

    answered_post = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]
    not_answered_post = posts.loc[(posts['PostTypeId'] == 1) & (posts['AcceptedAnswerId'].isnull())]

    AcAn_time = list()
    for question in answered_post.iterrows():
        if str(question[1]['LastEditDate']) != 'nan' and str(question[1]['LastEditDate']) != '-1':
            editDate = postsHistory.loc[((postsHistory['PostId'] == question[1]['Id']) & ((postsHistory['PostHistoryTypeId'] == 4) | (postsHistory['PostHistoryTypeId'] == 5) | (postsHistory['PostHistoryTypeId'] == 6) |(postsHistory['PostHistoryTypeId'] == 24)))]
            editDate['CreationDate'] =pd.to_datetime(editDate.CreationDate)
            editDate = editDate.sort_values('CreationDate')
            editDate = editDate.iloc[0]
            element = datetime.datetime.strptime(str(editDate[4]), "%Y-%m-%d %H:%M:%S.%f")
            tuple = element.timetuple()
            lastEditTime = time.mktime(tuple)

            answerPost = posts.loc[posts['Id'] == question[1]['AcceptedAnswerId']]
            answerTime = answerPost['CreationDate'].values

            element = datetime.datetime.strptime(answerTime[0], "%Y-%m-%dT%H:%M:%S.%f")
            tuple = element.timetuple()
            answerTime = time.mktime(tuple)

            if lastEditTime > answerTime:
                AcAn_time.append(copy.deepcopy(1))
            else:
                AcAn_time.append(copy.deepcopy(0))

    time_dur = AcAn_time
    AcAn_ones = [1] * len(AcAn_time)
    one_zeros = AcAn_ones
    corr = np.corrcoef(one_zeros, time_dur)

    print("edit correlation = " + str(corr))

    corr, _ = spearmanr(one_zeros, time_dur)
    print('Spearmans correlation: %.3f' % corr)


correlation()