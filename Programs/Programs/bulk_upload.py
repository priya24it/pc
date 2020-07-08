#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from elasticsearch import Elasticsearch, helpers
import os, uuid
import settings

# create a new instance of the Elasticsearch client class
elastic = Elasticsearch()
# ...or uncomment to use this instead:
#elastic = Elasticsearch("localhost")

'''
a simple function that gets the working path of
the Python script and returns it
'''
def script_path():
    path = os.path.dirname(os.path.realpath(__file__))
    if os.name == 'posix': # posix is for macOS or Linux
        path = path + "/"
    else:
        path = path + chr(92) # backslash is for Windows
    return path


'''
this function opens a file and returns its
contents as a list of strings split by linebreaks
'''
def get_data_from_file(self, path=script_path()):
    file = open(path + str(self), encoding="utf8", errors='ignore')
    data = [line.strip() for line in file]
    file.close()
    return data

'''
generator to push bulk data from a JSON
file into an Elasticsearch index
'''
def bulk_json_data(json_file, _index, doc_type):
    json_list = get_data_from_file(json_file)
    for doc in json_list:
        print(doc)

    for doc in json_list:
    # use a `yield` generator so that the data
    # isn't loaded into memory
        if '{"index"' not in doc:
            yield {
                "_index": _index,
                "_type": doc_type,
                "_id": uuid.uuid4(),
                "_source": doc
            }

def bulk_index():
    try:
        # make the bulk call, and get a response
        response = ""
        #print("bulk json data in the HI file")
        #print("json data")
        # print("rpd.json")
        print(bulk_json_data("rpd.json",settings.INDEX_NAME, settings.TYPE_NAME))
        response = helpers.bulk(elastic, bulk_json_data("rpd.json", settings.INDEX_NAME,settings.TYPE_NAME))
        print ("\nbulk_json_data() RESPONSE:", response)
    except Exception as e:
        print("\nERROR:", e)


#bulk_index()
