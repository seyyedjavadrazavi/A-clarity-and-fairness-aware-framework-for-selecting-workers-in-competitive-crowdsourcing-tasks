import pandas as pd
import numpy as np
import copy
from csv import writer

sim_work = pd.read_csv(r"./similar_works.csv")

sim_work.columns = ['wrk_id', 'sim_wrk_id', 'similarity']

work_id = sim_work.drop_duplicates(subset=['wrk_id'])
first = True

for wrk in work_id.iterrows():
    sim_wrks = sim_work.loc[(sim_work['wrk_id'] == wrk[1]['wrk_id']) & (sim_work['similarity'] > 0.3)]
    # for i in sim_wrks.iterrows():
    #     print(i[1].values[2])

    sim_wrks = sim_wrks.sort_values(by=['similarity'], ascending=False)

    top_50 = sim_wrks.iloc[:100]

    with open('more_Then_30_prnt_simi.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        if first == True:
            writer_object.writerow(['wrk_id', 'sim_wrk_id', 'similarity'])
            first = False
        
        for ii in top_50.iterrows():
            writer_object.writerow(ii[1].values)
        f_object.close()
