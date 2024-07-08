import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import copy

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")

answered_post = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]
not_answered_post = posts.loc[(posts['PostTypeId'] == 1) & (posts['AcceptedAnswerId'].isnull())]

AcAn_completion_rate = list()
for question in answered_post.iterrows():
    userPosts_qu = posts.loc[((posts['OwnerUserId'] == question[1]['OwnerUserId']) & (posts['PostTypeId'] == 1))]
    userPosts_AcAn = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull()) & (posts['OwnerUserId'] == question[1]['OwnerUserId'])]
    ### devide by zero
    if len(userPosts_qu) == 0: 
        AcAn_completion_rate.append(copy.deepcopy(0))
    else:
        AcAn_completion_rate.append(copy.deepcopy(len(userPosts_AcAn) / len(userPosts_qu)))

not_AcAn_completion_rate = list()
for question in not_answered_post.iterrows():
    userPosts_qu = posts.loc[((posts['OwnerUserId'] == question[1]['OwnerUserId']) & (posts['PostTypeId'] == 1))]
    userPosts_AcAn = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull()) & (posts['OwnerUserId'] == question[1]['OwnerUserId'])]
    ### devide by zero
    if len(userPosts_qu) == 0: 
        not_AcAn_completion_rate.append(copy.deepcopy(0))
    else:
        not_AcAn_completion_rate.append(copy.deepcopy(len(userPosts_AcAn) / len(userPosts_qu)))

edit = AcAn_completion_rate + not_AcAn_completion_rate

AcAn_ones = [1] * len(AcAn_completion_rate)
not_AcAn_zeros = [0] * len(not_AcAn_completion_rate)
one_zeros = AcAn_ones + not_AcAn_zeros

corr = np.corrcoef(one_zeros, edit)

print("completion_rate correlation = " + str(corr))

corr, _ = spearmanr(one_zeros, edit)
print('Spearmans correlation: %.3f' % corr)