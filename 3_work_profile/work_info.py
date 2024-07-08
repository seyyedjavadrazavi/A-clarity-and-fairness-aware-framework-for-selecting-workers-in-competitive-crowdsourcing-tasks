import pandas as pd
import copy
from csv import writer

users = pd.read_csv(r"../1_prepration/Users/Users.csv")
posts = pd.read_csv(r"../1_prepration/Posts/Posts.csv")
tags = pd.read_csv(r"../1_prepration/Tags/Tags.csv")

questions = posts.loc[(posts['PostTypeId'] == 1) & (~posts['AcceptedAnswerId'].isnull())]

new_columns = list()
new_columns.append(copy.deepcopy('Id'))
for i in tags['TagName']:
    new_columns.append(copy.deepcopy(i))

with open('./work_info.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(new_columns)
    f_object.close()

work_info = list()
for qu in questions.iterrows():
  total_tag = list()

  for i in range(len(tags['Id'])):
    total_tag.append(copy.deepcopy(int(0)))

  if (str(qu[1]['Tags']) != 'nan'):
    qu_tag = qu[1]['Tags']
    qu_tag = qu_tag.replace('<', '')
    qu_tag = qu_tag.split('>')
    qu_tag.remove('')

    for tg in qu_tag:
        tag_id = tags.loc[tags['TagName'] == tg]
        if (tag_id.empty != True):
            index = int(tag_id.index[0])
            total_tag[index] += 1

  total_tag.insert(0, qu[1]['Id'])
  # work_info.append(copy.deepcopy(total_tag))

  with open('./work_info.csv', 'a', newline='') as f_object:  
      writer_object = writer(f_object)
      writer_object.writerow(total_tag)
      f_object.close()


# xml_df = pd.DataFrame(work_info, columns=new_columns)

# xml_df.to_csv(r"./work_info.csv", index = False, header=True)