import pandas as pd
import xml.etree.ElementTree as et
from lxml import etree

df_cols = ["Id", "PostId", "Score", "Text", "CreationDate", "UserId", "ContentLicense"]

parser = etree.XMLParser(recover=True)
root = et.parse("./Comments.xml", parser = parser)
rows= root.findall('.//row')

xml_data = [[row.get("Id"), row.get("PostId"), row.get("Score"), row.get("Text"), row.get("CreationDate"), row.get("UserId"), row.get("ContentLicense")] for row in rows]

xml_df = pd.DataFrame(xml_data, columns=df_cols) 

xml_df.to_csv(r"./Comments.csv", index = False, header=True)
