import time
import sys
#from imp

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

#reload(sys)
#sys.setdefaultencoding('utf-8')

def set_mapping(es, index_name = "content_engine17", doc_type_name = "en10",include_type_name=False):

    my_mapping= { "mappings": {
        "en10": {
            "properties": {
                "age": {"type": "long"},
                "experience": {"type": "long"},
                "name": {"type": "text"}
            }
        }
    }
    }
    create_index = es.indices.create(index = index_name,body = my_mapping,include_type_name=True)
    print(create_index)
   # mapping_index = es.indices.put_mapping(index = index_name, doc_type = doc_type_name, body = my_mapping,include_type_name=True)
   # print(mapping_index)
   # if create_index["acknowledged"] != True or mapping_index["acknowledged"] != True:
       # print("Index creation failed...")

def set_data(es, input_file, index_name = "content_engine", doc_type_name="en"):
    i = 0
    count = 0
    ACTIONS = []
    for line in open(input_file):
        fields = line.replace("\r\n", "").replace("\n", "").split("----")
        if len(fields) == 2:
            a, b = fields
        else:
            continue
        action = {
            "_index": index_name,
            "_type": doc_type_name,
            "_source": {
                  "a": a,
                  "b": b,
            }
        }
        i += 1
        ACTIONS.append(action)
        if (i == 500000):
            success, _ = bulk(es, ACTIONS, index = index_name, raise_on_error = True)
            count += success
            i = 0
            ACTIONS = []

    success, _ = bulk(es, ACTIONS, index = index_name, raise_on_error=True)
    count += success
    print("insert %s lines" % count)


if __name__ == '__main__':
    es = Elasticsearch(hosts="http://localhost:9200", timeout=5000)
    #set_mapping(es)
    set_data(es,sys.argv[1])