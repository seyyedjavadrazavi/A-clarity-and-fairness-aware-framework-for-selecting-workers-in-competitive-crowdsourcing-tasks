import copy
import pandas as pd
import numpy as np
from scipy.stats import spearmanr

posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")

answered_post = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]
not_answered_post = posts.loc[(posts['PostTypeId'] == 1) & (posts['AcceptedAnswerId'].isnull())]

AcAn_edited = list()
for x in answered_post['LastEditorUserId']:
    if str(x) == 'nan':
        AcAn_edited.append(copy.deepcopy(1))
    else:
        AcAn_edited.append(copy.deepcopy(0))

not_AcAn_edited = list()
for y in not_answered_post['LastEditorUserId']:
    if str(y) == 'nan':
        not_AcAn_edited.append(copy.deepcopy(1))
    else:
        not_AcAn_edited.append(copy.deepcopy(0))

edit = AcAn_edited + not_AcAn_edited

AcAn_ones = [1] * len(AcAn_edited)
not_AcAn_zeros = [0] * len(not_AcAn_edited)
one_zeros = AcAn_ones + not_AcAn_zeros

corr = np.corrcoef(one_zeros, edit)

print("edit correlation = " + str(corr))

corr, _ = spearmanr(one_zeros, edit)
print('Spearmans correlation: %.3f' % corr)