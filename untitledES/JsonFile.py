import requests
import json
import pandas as pd
import time

from xl2dict import XlToDict

databasename = "employees"
tablename = "people"
tablestructure =  {"settings": {"mappings": {"properties": {"name": {"type": "text"}, "sex": {"type": "text"}, "age": {"type": "string" } ,"years": {"type": "text"} }}}}
tabledata = ""
header = {"Content-type": "application/json"}

print("converting excel data into Json data")
myxlobject= XlToDict()
data = myxlobject.convert_sheet_to_dict(file_path="person.xlsx", sheet="Sheet1")
print(len(data))
outfile = "person2.json"
newJson = json.dumps(data, indent=None, separators=(',', ':'))
print(newJson[0])
for obj in range(0,len(data)):
    newJson = json.dumps(data, indent=None, separators=(',', ':'))

    print(data[obj])
#with open('person2.json', 'w') as json_file:
    #json_file.write(newJson+"\n")
#with open('person2.json', 'w',newline='\n') as outfile:
 #   json.dump(data, outfile)
with open('person2.json', 'w',newline="\n") as outfile:
    json.dump(newJson, outfile, indent=None)

for i in range(0,len(data)):
    #print(data[i])
    tabledata = json.dumps(data[i], separators=(',', ':'))
    with open("person.json", "a") as outfile:
        outfile.write(tabledata+"\n")
    #print("JSON Data")
    #print(tabledata)
    print("inserting json data into the table")
    InsertQuery = "http://localhost:9200/"+databasename+"/"+tablename
    #print("Insert query..."+str(InsertQuery))
    response = requests.post(InsertQuery,data= tabledata,headers=header)
    #print(response.text)
    time.sleep(4)