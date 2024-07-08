from sklearn.model_selection import train_test_split
import pandas as pd

infos = pd.read_csv(r"../8_similar_works/combination_of_profiles_similarities.csv")
infos = infos.drop_duplicates(subset=['workId'])

X = infos.loc[:, infos.columns != 'label']
y = infos[["label"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

df_cols = ['workId']
df = pd.DataFrame(X_test['workId'].values, columns=df_cols) 

df.to_csv(r"./testResultData.csv", index = False, header=True)

