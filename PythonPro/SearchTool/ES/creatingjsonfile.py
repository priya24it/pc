import  elasticsearch
import requests
import json
import pandas as pd
import time
from xl2dict import XlToDict
import settings


es  = elasticsearch.Elasticsearch()

def quick_search(client, query, limit):

    for i in range(settings.MAX_RETRIES):

        search_results = []
        response = client.search(index=settings.INDEX_NAME,
                                 doc_type=settings.TYPE_NAME,
                                 body=query,
                                 size=limit)

        if 'hits' not in response:
            time.sleep(settings.RETRY_DELAY)
            continue

        if limit == settings.QUICK_SEARCH_SIZE:
            if response['hits']['total'] > settings.MAX_RESULT_SIZE:
                print('Result size exceed Max Result Window', len(response['hits']['hits']))
                return search_results
            else:
                response = client.search(index=settings.INDEX_NAME,
                                         doc_type=settings.TYPE_NAME,
                                         body=query,
                                         size=settings.MAX_RESULT_SIZE)

        found = {}
        for doc in response['hits']['hits']:
            doc = doc['_source']
            key = '{0}:{1}'.format(doc['expressionId'], doc['key'])
            if key not in found:
                search_results.append(doc)
                found[key] = True
        return search_results



def to_camel_case(field):
    return field[0].lower() + field[1:]

def new_terms_query(rpd, terms):
    query = {
        'query': {
            'constant_score': {
                'filter': {
                    'terms': {
                        to_camel_case(rpd): terms
                    }
                }
            }
        }
    }
    return query


print("converting excel data into Json data")
'''myxlobject1 = XlToDict()
data = myxlobject1.convert_sheet_to_dict("InputData.xlsx")
tabledata = json.dumps(data, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(tabledata)
print("JSON Data")
print(tabledata)'''

query = "http://localhost:9200/rpd15/rpddata15/61950856-15cd-485f-89d2-4acebda4de1e"
print(query)
response = requests.get(query,verify='False')
print(response.text)
terms = json.loads(response.text)
total_terms = len(terms)
page_count = int(total_terms / settings.TERM_QUERY_BATCH_SIZE) + 1

result = []
for page in range(page_count):
    skip = page * settings.TERM_QUERY_BATCH_SIZE
    till = (page + 1) * settings.TERM_QUERY_BATCH_SIZE
    till = total_terms if till > total_terms else till
   # items = terms[1:3]

query = new_terms_query('rpd', terms)
response = es.search(index=settings.INDEX_NAME,
                         doc_type=settings.TYPE_NAME,
                         body=query,
                         size=settings.MAX_RESULT_SIZE)

