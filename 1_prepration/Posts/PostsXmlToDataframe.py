import pandas as pd
import xml.etree.ElementTree as et

df_cols = ["Id", "PostTypeId", "AcceptedAnswerId", "ParentId", "CreationDate", "Score", "Body", 
"ViewCount", "OwnerUserId", "LastEditorUserId", "LastEditDate", "LastActivityDate", "Title", "Tags", "AnswerCount", "CommentCount",
"FavoriteCount", "ClosedDate", "CommunityOwnedDate"]

root = et.parse("./Posts.xml")
rows= root.findall('.//row')

xml_data = [[row.get("Id"), row.get("PostTypeId"), row.get("AcceptedAnswerId"), row.get("ParentId"), row.get("CreationDate"),
 row.get("Score"), row.get("Body"), row.get("ViewCount"), row.get("OwnerUserId"), row.get("LastEditorUserId"), 
 row.get("LastEditDate"), row.get("LastActivityDate"), row.get("Title"), row.get("Tags"), row.get("AnswerCount"),
 row.get("CommentCount"), row.get("FavoriteCount"), row.get("CommunityOwnedDate"), row.get("ClosedDate")] for row in rows]

xml_df = pd.DataFrame(xml_data, columns=df_cols) 

xml_df.to_csv(r"./Posts.csv", index = False, header=True)