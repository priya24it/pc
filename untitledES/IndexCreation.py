import requests
import json
import pandas as pd
import time
from xl2dict import XlToDict

databasename = "employees100"
tablename = "people100"
#tablestructure =  {"settings": {"mappings": {"properties": {"name": {"type": "text"}, "sex": {"type": "text"}, "age": {"type": "string" } ,"years": {"type": "text"} }}}}
tabledata = ""
header = {"Content-type": "application/json"}
#working structure.
tablestructure = {"mappings": { "doc": { "properties": { "speaker": {"type": "keyword"}, "play_name": {"type": "keyword"}, "line_id": {"type": "integer"}, "speech_number": {"type": "integer"} } } } }

print("creating Index and table ...")
query = "http://localhost:9200/"+databasename+"/"+tablename
response = requests.post(query,data= json.dumps(tablestructure),headers=header)
print(response.text)
print("database and table has created successfully....")


