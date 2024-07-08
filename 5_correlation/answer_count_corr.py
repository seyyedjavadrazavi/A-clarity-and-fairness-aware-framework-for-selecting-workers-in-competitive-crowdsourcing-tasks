import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import copy

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")

answered_post = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]
not_answered_post = posts.loc[(posts['PostTypeId'] == 1) & (posts['AcceptedAnswerId'].isnull())]

AcAn_answer_No = list()
for x in answered_post['AnswerCount']:
    if str(x) == 'nan':
        AcAn_answer_No.append(copy.deepcopy(0)) 
    else:
        AcAn_answer_No.append(copy.deepcopy(x)) 
         

not_AcAn_answer_No = list()
for x in not_answered_post['AnswerCount']:
    if str(x) == 'nan':
        not_AcAn_answer_No.append(copy.deepcopy(0)) 
    else:
        not_AcAn_answer_No.append(copy.deepcopy(x)) 

answer = AcAn_answer_No + not_AcAn_answer_No

AcAn_ones = [1] * len(AcAn_answer_No)
not_AcAn_zeros = [0] * len(not_AcAn_answer_No)
one_zeros = AcAn_ones + not_AcAn_zeros

corr = np.corrcoef(one_zeros, answer)

print("answerent correlation = " + str(corr))

corr, _ = spearmanr(one_zeros, answer)
print('Spearmans correlation: %.3f' % corr)