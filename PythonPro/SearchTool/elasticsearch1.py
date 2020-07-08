from xl2dict import XlToDict

import Common
import database
import os
import pandas as pd
from pandas import *
import json
import requests
import request


ce = Common.common

class Elasticsearch1(Common.common):

    ce = Common.common

    def preprocess(self,SourceFile):
        log = Common.common.getlogger(self)
        log.info("started loading the Excel file")
        excel_data = database.load_excel(SourceFile)
        log.info("Total number of rows and columns in Excel source" + str(excel_data.shape))
       # csvfile = database.convert_toCSV(excel_data)

        jsondata = database.convert_toJSON(excel_data)
        #log.info(jsondata)

    def load_data(self,CSV_Filename):
        database.load_intoDBTable(CSV_Filename)

    def create_index(self):
        database.create_index()

    def search_results(self):
        database.search_results()

    def execution_time(self):
        database.execution_time()

SourceFile = r"InputData.xlsx"
JsonFile = r"C:\Python Pro\untitled\InputData.json"
#os.remove(r"logfile.log")
s = Elasticsearch1()

"""myxlobject= XlToDict()
data = myxlobject.convert_sheet_to_dict(file_path="InputData.xlsx", sheet="Sheet1")
print(data)
json_object = json.dumps(data, indent=4)
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)"""


def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


response = requests.get("http://localhost:9200/")
print(response.status_code)

pload =  {"query": {"match": {"age": {"query": "6"}}}}  #singlesearch
multiplesearch = {"query": {"multi_match": {"query": "Anu 6", "fields": ["name", "Age"]}}}
print(multiplesearch)
header = {"Content-type": "application/json"
            }
print(json.dumps(pload))
#response = requests.post("http://localhost:9200/company/employee/",data=json.dumps(pload),headers=header) #creating a database
#print(response.text)


pload =  {"query": {"match": {"age": {"query": "6"}}}}  #singlesearch
multiplesearch = {"query": {"multi_match": {"query": "Anu 6", "fields": ["name", "Age"]}}}

#Singlesearch
response2 = requests.post("http://localhost:9200/company/employee/_search",data= json.dumps(pload),headers=header) #creating a database
print(response2.text)
d = json.loads(response2.text)
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

#Multiplesearch
response2 = requests.post("http://localhost:9200/company/employee/_search",data= json.dumps(multiplesearch),headers=header) #creating a database
print(response2.text)

d = json.loads(response2.text)
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


#xls = ExcelFile(SourceFile)
#data = xls.parse(xls.sheet_names[0],orient='records')
#print(data.to_dict())

#s.preprocess(SourceFile)
#s.load_data()
#s.search_results()
#s.execution_time()
