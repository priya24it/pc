import numpy
import pandas
from elasticsearch import Elasticsearch, helpers
import os, uuid
import settings
import pandas as pd

es = Elasticsearch()

body = {
    "query": {
        "multi_match": {
            "query": "Praveen Japan",
            "fields": ["Author", "Title"]
        }
    }
}

response = es.search(index=settings.INDEX_NAME, doc_type=settings.TYPE_NAME, body=body,size=10000)
print(response)

fields = {}
for key, val in response["hits"].items():
    if key == "hits":
        for num, doc in enumerate(val):
           source_data = doc["_source"]
           for key, val in source_data.items():
               try:
                   fields[key] = numpy.append(fields[key], val)
               except KeyError:
                   fields[key] = numpy.array([val])

#for key, val in fields.items():
   # print (key, "--->", val)
#    print ("NumPy array len:", len(val), "\n")

# create a Pandas DataFrame array from the fields dict
elastic_df = pandas.DataFrame(fields)

print ('elastic_df:', type(elastic_df), "\n")
#print (elastic_df)
elastic_df.to_excel("finalresult.xlsx")