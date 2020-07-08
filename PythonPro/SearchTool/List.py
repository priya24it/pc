import requests
import json
import pandas as pd
import time

from xl2dict import XlToDict

databasename = "comp2"
tablename = "emp2"
tablestructure =  {"settings": {"mappings": {"properties": {"firstname": {"type": "text"}, "lastname": {"type": "text"}, "dob": {"type": "string" } ,"email": {"type": "text"} }}}}
tabledata = ""
header = {"Content-type": "application/json"}

print("converting excel data into Json data")
myxlobject= XlToDict()
data = myxlobject.convert_sheet_to_dict(file_path="InputData.xlsx", sheet="Sheet1")
print(len(data))
for i in range(0,len(data)):
    tabledata = json.dumps(data[i], separators=(',', ':'))
    with open("rpd.json", "a") as outfile:
        outfile.write(tabledata+"\n")



for i in range(0,1):
    print(data[i])
    tabledata = json.dumps(data[i], indent=2,separators=(',', ':'))
    with open("sample.json", "w") as outfile:
        outfile.write(tabledata + "\n")
    print("JSON Data")
    print(tabledata)
    print("inserting json data into the table")
    InsertQuery = "http://localhost:9200/"+databasename+"/"+tablename
    print("Insert query..."+str(InsertQuery))
    response = requests.post(InsertQuery,data= tabledata,headers=header)
    print(response.text)
    time.sleep(4)
