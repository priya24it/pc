import json
import pandas as pd
import time

import requests
from xl2dict import XlToDict

databasename = "contents"
tablename = "title"
#tablestructure =  {"settings": {"mappings": {"properties": {"name": {"type": "text"}, "sex": {"type": "text"}, "age": {"type": "string" } ,"years": {"type": "text"} }}}}
tabledata = ""
header = {"Content-type": "application/json"}
#working structure.
tablestructure = {"mappings": { "doc": { "properties": { "slug": {"type": "keyword"}, "title": {"type": "keyword"}, "content": {"type": "integer"} } } } }

print("creating Index and table ...")
query = "http://localhost:9200/"+databasename+"/"+tablename
response = requests.post(query,data= json.dumps(tablestructure),headers=header)
print(response.text)
print("database and table has created successfully....")