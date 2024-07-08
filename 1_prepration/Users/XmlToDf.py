import pandas as pd
import xml.etree.ElementTree as et

df_cols = ["Id", "Reputation", "CreationDate", "DisplayName", "LastAccessDate", "WebsiteUrl", "Location", 
"AboutMe", "Views", "UpVotes", "DownVotes", "ProfileImageUrl", "AccountId"]

root = et.parse("./Users.xml")
rows= root.findall('.//row')

xml_data = [[row.get("Id"), row.get("Reputation"), row.get("CreationDate"), row.get("DisplayName"), row.get("LastAccessDate"),
 row.get("WebsiteUrl"), row.get("Location"), row.get("AboutMe"), row.get("Views"), row.get("UpVotes"), 
 row.get("DownVotes"), row.get("ProfileImageUrl"), row.get("AccountId")] for row in rows]

xml_df = pd.DataFrame(xml_data, columns=df_cols) 

xml_df.to_csv(r"./Users.csv", index = False, header=True)