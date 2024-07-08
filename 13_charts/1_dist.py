import matplotlib.pyplot as plt
import pandas as pd

original = pd.read_csv(r"../12_suitability_score/ourself/50_top_person_all_wrkrs_not_1_new.csv")
china = pd.read_csv(r"../12_suitability_score/china/50_top_person_all_tags.csv")
sharif = pd.read_csv(r"../12_suitability_score/sharif/50_top_person_all_tags.csv")

org = original['similarity']
chn = china['similarity']
shr = sharif['similarity']

fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(5, 5))
ax0.hist(org, 10, histtype='bar', color = 'red', hatch="///////")
ax0.set_title('Our Model')
ax0.set(xlim=(0, 1), ylim=(0, 80000))
ax0.set_yticks([10000, 20000, 40000, 60000, 80000])

s = pd.Series(org)
ax1 = s.plot.kde()
ax1.set(xlim=(0, 1))

fig.tight_layout()
plt.show()

fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(5, 5))
ax0.hist(shr, 10, histtype='bar', color = 'red', hatch="///////")
ax0.set_title('ASTE')
ax0.set(xlim=(0, 1), ylim=(0, 80000))
ax0.set_yticks([10000, 20000, 40000, 60000, 80000])

s = pd.Series(shr)
ax1 = s.plot.kde()
ax1.set(xlim=(0, 1))

fig.tight_layout()
plt.show()


fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(5, 5))
ax0.hist(chn, 10, histtype='bar', color = 'red', hatch="///////")
ax0.set_title('BRE')
ax0.set(xlim=(0, 1), ylim=(0, 80000))
ax0.set_yticks([10000, 20000, 40000, 60000, 80000])

s = pd.Series(chn)
ax1 = s.plot.kde()
ax1.set(xlim=(0, 1))

fig.tight_layout()
plt.show()

