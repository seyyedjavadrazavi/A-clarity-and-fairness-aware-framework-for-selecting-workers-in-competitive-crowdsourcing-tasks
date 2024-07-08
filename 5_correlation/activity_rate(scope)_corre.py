from typing import Counter
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import copy

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")
tags = pd.read_csv(r"../1_prepration/Tags/Tags.csv")
users = pd.read_csv(r"../1_prepration/Users/Users.csv")
users_profile = pd.read_csv(r"../2_requester_profile/requester_profile.csv")

answered_post = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]
not_answered_post = posts.loc[(posts['PostTypeId'] == 1) & (posts['AcceptedAnswerId'].isnull())]

AcAn_activity_rate_scope = list()
for question in answered_post.iterrows():

    a = question[1]['Tags'].find('c++')
    if(type(question[1]['Tags']) != float): #& (question[1]['Tags'].find('++') == -1):
        qu_tag = question[1]['Tags']
        qu_tag = qu_tag.replace('<', '')
        qu_tag = qu_tag.split('>')
        qu_tag.remove('')

        profile = users_profile.loc[(users_profile['UserId'] == question[1]['OwnerUserId'])]

        scope_score = 0
        for tag in qu_tag:
            col_index = 0
            pr_col = list(profile.columns.values) 
            for col in pr_col:
                if col == tag:
                    scope_score += profile[col_index].values
                else:
                    col_index += 1
        
        AcAn_activity_rate_scope.append(copy.deepcopy(scope_score/len(tags)))


not_AcAn_activity_rate_scope = list()
for question in not_answered_post.iterrows():
    if(type(question[1]['Tags']) != float):
        tags = question[1]['Tags']    
        tags = tags.replace('<', '')
        tags = tags.split('>')
        tags.remove('')

        profile = users_profile.loc[(users_profile['UserId'] == question[1]['OwnerUserId'])]

        scope_score = 0
        for tag in qu_tag:
            col_index = 0
            for col in profile.columns():
                if col == tag:
                    scope_score += profile[col_index].values
                else:
                    col_index += 1
        
        not_AcAn_activity_rate_scope.append(copy.deepcopy(scope_score/len(tags)))


scope = AcAn_activity_rate_scope + not_AcAn_activity_rate_scope

AcAn_ones = [1] * len(AcAn_activity_rate_scope)
not_AcAn_zeros = [0] * len(not_AcAn_activity_rate_scope)
one_zeros = AcAn_ones + not_AcAn_zeros

corr = np.corrcoef(one_zeros, scope)

print("activity_rate_scope correlation = " + str(corr))

corr, _ = spearmanr(one_zeros, scope)
print('Spearmans correlation: %.3f' % corr)