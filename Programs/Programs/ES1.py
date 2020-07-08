import numpy
import pandas
from elasticsearch import Elasticsearch, helpers
import os, uuid
import settings
import pandas as pd

es = Elasticsearch()

body = {
  "query": {
    "match": {
      "rpddata": {
        "query": "annual praveen ja",
        "operator": "and"
      }
    }
  }
}



response = es.search(index="rpd32", doc_type="_doc", body=body,size=6000)
print(response)

#body = {"POST my_index/_refresh"}

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

for key, val in fields.items():
    print (key, "--->", val)
    print ("NumPy array len:", len(val), "\n")

# create a Pandas DataFrame array from the fields dict
elastic_df = pandas.DataFrame(fields)

print ('elastic_df:', type(elastic_df), "\n")
print (elastic_df)
elastic_df.to_excel("finalresult.xlsx")

