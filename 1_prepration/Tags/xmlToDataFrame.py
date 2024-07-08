import pandas as pd
import xml.etree.ElementTree as et

root = et.parse("./Tags.xml")
rows = root.findall(".//row")

df_cloumns = ["Id", "TagName", "Count", "ExcerptPostId", "WikiPostId"]

xml_data = [[row.get("Id"), row.get("TagName"), row.get("Count"), row.get("ExcerptPostId"), row.get("WikiPostId")]
for row in rows]

df_tags = pd.DataFrame(data=xml_data, columns=df_cloumns)

df_tags.to_csv(r"./Tags.csv", index=False, header=True)