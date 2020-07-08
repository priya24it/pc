import requests
import json
import pandas as pd

from xl2dict import XlToDict

databasename = "comp2"
tablename = "emp2"
tablestructure =  {"settings": {"mappings": {"properties": {"firstname": {"type": "text"}, "lastname": {"type": "text"}, "dob": {"type": "string" } ,"email": {"type": "text"} }}}}
tabledata = ""
header = {"Content-type": "application/json"}


def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


print("converting excel data into Json data")
myxlobject= XlToDict()
data = myxlobject.convert_sheet_to_dict(file_path="Sample.xlsx", sheet="Sheet1")
#data = str(data)[1:-1]
#print(data)
tabledata = json.dumps(data, indent=4)
print(tabledata)
with open("sample.json", "w") as outfile:
    outfile.write(tabledata)
print("JSON Data")
print(tabledata)


print(tablestructure)
response = requests.get("http://localhost:9200/") #creating a database
print("Elastic serach is up and running "+str(response.text))


''' 
print("creating Index and table ...")
query = "http://localhost:9200/"+databasename+"/"+tablename
response = requests.post(query,data= json.dumps(tablestructure),headers=header)
print(response.text)
print("database and table has created successfully....")  '''

print("verify whether given database and table  exists .. .")
query = "http://localhost:9200/"+databasename+"/"+tablename+"/_search?pretty=true"
print(query)
response = requests.get(query,verify='False')
print(response.text)
d = json.loads(response.text)
print(type(d))
finaldata = flatten_dict(d)
subDict = finaldata['hits_hits']
print(subDict)
df = pd.DataFrame(subDict)
finalDict = dict(df['_source'])
print(finalDict)
df = pd.DataFrame(finalDict)
df = df.T
print(df)



'''
print("inserting json data into the table")
InsertQuery = "http://localhost:9200/"+databasename+"/"+tablename
print("Insert query..."+str(InsertQuery))
response = requests.post(InsertQuery,data= data,headers=header)
print(response.text) '''



























