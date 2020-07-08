import requests
import json
import pandas as pd
import time
from xl2dict import XlToDict

databasename = "rpd4"
tablename = "rpddata4"
tablestructure =  {"settings": {"mappings": {"properties": {"firstname": {"type": "text"}, "lastname": {"type": "text"}, "dob": {"type": "string" } ,"email": {"type": "text"} }}}}
tabledata = ""
header = {"Content-type": "application/json"}

print("creating Index and table ...")
query = "http://localhost:9200/"+databasename+"/"+tablename
response = requests.post(query,data= json.dumps(tablestructure),headers=header)
print(response.text)
print("database and table has created successfully....")

print("converting excel data into Json data")
myxlobject= XlToDict()
data = myxlobject.convert_sheet_to_dict(file_path=r"InputData.xlsx", sheet="Sheet1")
print(len(data))
#data = data[0]
#print(data[0])
tabledata = json.dumps(data, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(tabledata)
print("JSON Data")
print(tabledata)
"""
print("inserting json data into the table")
InsertQuery = "http://localhost:9200/"+databasename+"/"+tablename
print("Insert query..."+str(InsertQuery))
response = requests.post(InsertQuery,data= tabledata,headers=header)
print(response.text)
time.sleep(4) """

