import requests
import json
import pandas as pd
import time
from xl2dict import XlToDict

databasename = "rpd3"
tablename = "rpddata3"
tablestructure =  {"settings": {"mappings": {"properties": {"firstname": {"type": "text"}, "lastname": {"type": "text"}, "dob": {"type": "string" } ,"email": {"type": "text"} }}}}
tabledata = ""
header = {"Content-type": "application/json"}

def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }

data = pd.read_excel("InputData.xlsx")
df = pd.DataFrame(data)
columns = df.columns.values.tolist()
columnname = ""
finalstructure = '{"settings": {"mappings": {"properties": {'
for i in range(0,len(columns)):
    columnname= '"'+columns[i]+'":{"type": "text"}, '
    finalstructure = finalstructure + columnname
finalstructure = finalstructure[0:len(finalstructure)-1]
finalstructure =   finalstructure + " }}}}"
print(finalstructure)


myxlobject= XlToDict()
data = myxlobject.convert_sheet_to_dict(file_path=r"InputData.xlsx", sheet="Sheet1")
print("converting excel data into Json data")
print(len(data))



for i in range(0,len(data)):
    tabledata = json.dumps(data[0], indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(tabledata)
    print("JSON Data")
    print(tabledata)
    print("inserting json data into the table")
    InsertQuery = "http://localhost:9200/"+databasename+"/"+tablename
    print("Insert query..."+str(InsertQuery))
    response = requests.post(InsertQuery,data= tabledata,headers=header)
    print(response.text)
    time.sleep(4)


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










