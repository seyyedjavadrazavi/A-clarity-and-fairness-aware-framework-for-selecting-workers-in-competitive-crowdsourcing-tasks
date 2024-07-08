import pandas as pd
import xml.etree.ElementTree as et

df_cols = ["Id", "PostHistoryTypeId", "PostId", "RevisionGUID"
, "CreationDate", "UserId", "Text", "ContentLicense"]

root = et.parse("./PostHistory.xml")
rows = root.findall('.//row')

# NESTED LIST
xml_data = [[row.get('Id'), row.get('PostHistoryTypeId'), row.get('PostId'), row.get('RevisionGUID'),
row.get('CreationDate'), row.get('UserId'), row.get('Text'), row.get('ContentLicense')] for row in rows]

df_xml = pd.DataFrame(xml_data, columns=df_cols)

df_xml.to_csv (r"./postsHistory.csv", index = False, header=True)