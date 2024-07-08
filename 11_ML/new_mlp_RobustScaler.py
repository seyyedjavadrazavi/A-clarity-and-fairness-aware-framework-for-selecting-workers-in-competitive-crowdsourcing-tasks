from sklearn.neural_network import MLPClassifier
# from sklearn import metrics
from imblearn.over_sampling import RandomOverSampler
# from sklearn.metrics import accuracy_score
import pandas as pd
# import copy
# import numpy as np
from csv import writer
# from sklearn import preprocessing
from sklearn.metrics import precision_recall_fscore_support

infos = pd.read_csv(r"../10_train_data/combination_of_profiles_similarities_intersection_sim.csv")
test_data = pd.read_csv(r"../9_test_data/needed_testData_profiles_round_40_intersection_sim.csv")

test_data = test_data.dropna(how = "all") 
test_id = test_data['workId'].unique()
infos = infos[~infos['workId'].isin(test_id)]
train_wrk_id = infos['workId'].values.tolist()

X = infos.loc[:, infos.columns != 'label']
X = X.loc[:, X.columns != 'req_qu_sim']
X = X.loc[:, X.columns != 'qu_qu_sim']
X_train = X.iloc[:, 3:]

Y_train = infos[["label"]]
Y_train_1 = infos.loc[infos["label"] == 1]
Y_train_1 = Y_train_1.drop_duplicates()
Y_train_0 = infos.loc[infos["label"] == 0]

ros = RandomOverSampler(random_state=1)
X_train_rb, Y_train = ros.fit_resample(X_train, Y_train)

# X_train_rb = X_train

# clf = MLPClassifier(solver='sgd', alpha=0.001, activation='relu', learning_rate_init=0.001, ############# after comment rb_scale.fit_transform, this came to be the best -> 1.0 
#                     hidden_layer_sizes=(8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)


# res = clf.score(X_train_rb, Y_train)
# print(res)
# y_pred = clf.predict(X_train_rb)
# print('Accuracy: {:.2f}'.format(accuracy_score(Y_train, y_pred)))


Y_test = test_data[["label"]]
input_data_tmp = test_data.loc[:, test_data.columns != 'label']
input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'req_qu_sim']
input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'qu_qu_sim']
# input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'workId']
# input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'similar_work_id']
# input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'requesterId']
# input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'workerId']
X_test = input_data_tmp.iloc[:, 4:]

# y_pred = clf.predict(X_test)

# per = precision_recall_fscore_support(y_pred, Y_test)

# print(per)

# cl_name = test_data.columns.values

# with open('res_RobustScaler_scaler_jacard_v2_40.csv', 'w', newline='') as f_object:  
#     writer_object = writer(f_object)
#     writer_object.writerow(cl_name)
#     f_object.close()

# cnt = 0
# for i in test_id:
#     input_data = []
#     input_data = test_data.loc[test_data['workId'] == i]
    
#     Y_test = input_data[["label"]]

#     input_data_tmp = input_data.loc[:, input_data.columns != 'label']
#     input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'req_qu_sim']
#     input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'similar_work_id']
#     input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'qu_qu_sim']
#     data = input_data_tmp.iloc[:, 3:]
    
#     y_pred = clf.predict(data)

#     per = precision_recall_fscore_support(y_pred, Y_test[:len(y_pred)])

    # input_data['label'] = y_pred

    # with open('res_RobustScaler_scaler_jacard_v2_40.csv', 'a', newline='') as f_object:  
    #     writer_object = writer(f_object)
    #     for j in input_data.iterrows():
    #         writer_object.writerow(j[1])
    #     f_object.close()


# clf = MLPClassifier(solver='adam', alpha=0.001, activation='relu', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)



# # X_test = rb_scale.fit_transform(X_test)

# # scaler = rb_scale.fit(data)
# # testX_scaled = scaler.transform(data)

# y_pred = clf.predict(X_test)

# res = clf.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)


# clf_1 = MLPClassifier(solver='adam', alpha=0.001, activation='logistic', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_1.predict(X_test)

# res = clf_1.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)

# clf_2 = MLPClassifier(solver='adam', alpha=0.001, activation='identity', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_2.predict(X_test)

# res = clf_2.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)
################################################## ++++++++++++++++++++++++++++++++
# clf_3 = MLPClassifier(solver='adam', alpha=0.001, activation='tanh', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_3.predict(X_test)

# res = clf_3.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)

# clf_log_3 = MLPClassifier(solver='sgd', alpha=0.001, activation='logistic', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_log_3.predict(X_test)

# res = clf_log_3.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)


# clf_log_4 = MLPClassifier(solver='sgd', alpha=0.001, activation='relu', learning_rate_init=0.001, ############# after comment rb_scale.fit_transform, this came to be the best -> 1.0 
#                     hidden_layer_sizes=(16, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_log_4.predict(X_test)

# res = clf_log_4.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)


# clf_log_5 = MLPClassifier(solver='sgd', alpha=0.001, activation='identity', learning_rate_init=0.001, ################## 0.8897 -> best up to now
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_log_5.predict(X_test)

# res = clf_log_5.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# # b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# # c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# # d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# # print(a)
# # print(b)
# # print(c)
# # print(d)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# clf_log_6 = MLPClassifier(solver='sgd', alpha=0.001, activation='tanh', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_log_6.predict(X_test)

# res = clf_log_6.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)

# clf_log_7 = MLPClassifier(solver='lbfgs', alpha=0.001, activation='relu', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_log_7.predict(X_test)

# res = clf_log_7.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)


# clf_log_8 = MLPClassifier(solver='lbfgs', alpha=0.001, activation='tanh', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_log_8.predict(X_test)

# res = clf_log_8.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)

# clf_log_9 = MLPClassifier(solver='lbfgs', alpha=0.001, activation='logistic', learning_rate_init=0.001, 
#                     hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

# y_pred = []
# y_pred = clf_log_9.predict(X_test)

# res = clf_log_9.score(X_test, Y_test)

# print(res)

# a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
# b = precision_recall_fscore_support(y_test, y_pred, average='micro')
# c = precision_recall_fscore_support(y_test, y_pred, average='weighted')
# d = precision_recall_fscore_support(y_test, y_pred, average='binary')

# print(a)
# print(b)
# print(c)
# print(d)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clf_log_10 = MLPClassifier(solver='lbfgs', alpha=0.001, activation='identity', learning_rate_init=0.001, 
                    hidden_layer_sizes=(64, 8, 1), random_state=1, learning_rate = 'constant').fit(X_train_rb, Y_train)

y_pred = []
y_pred = clf_log_10.predict(X_test)
per = precision_recall_fscore_support(Y_test, y_pred)

res = clf_log_10.score(X_test, Y_test)

print(res)

a = precision_recall_fscore_support(Y_test, y_pred, average='macro')
b = precision_recall_fscore_support(Y_test, y_pred, average='micro')
c = precision_recall_fscore_support(Y_test, y_pred, average='weighted')
d = precision_recall_fscore_support(Y_test, y_pred, average='binary')

print(a)
print(b)
print(c)
print(d)

cl_name = test_data.columns
with open('res_RobustScaler_scaler_jacard_v2_40.csv', 'w', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(cl_name)
    f_object.close()

cnt = 0
for i in test_id:
    input_data = []
    input_data = test_data.loc[test_data['workId'] == i]
    
    Y_test = input_data[["label"]]

    input_data_tmp = input_data.loc[:, input_data.columns != 'label']
    input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'req_qu_sim']
    input_data_tmp = input_data_tmp.loc[:, input_data_tmp.columns != 'qu_qu_sim']
    data = input_data_tmp.iloc[:, 4:]
    
    y_pred = clf_log_10.predict(data)

    per = precision_recall_fscore_support(y_pred, Y_test[:len(y_pred)])

    input_data['label'] = y_pred

    with open('res_RobustScaler_scaler_jacard_v2_40.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        for j in input_data.iterrows():
            writer_object.writerow(j[1])
        f_object.close()
