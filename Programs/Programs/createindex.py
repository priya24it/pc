
import numpy
import pandas
from elasticsearch import Elasticsearch, helpers
import os, uuid
import settings
import pandas as pd

es = Elasticsearch()


request_body =  {
   "settings": {
    "analysis": {
      "analyzer": {
        "autocomplete": {
          "tokenizer": "autocomplete",
          "filter": [
            "lowercase"
          ]
        },
        "autocomplete_search": {
          "tokenizer": "lowercase"
        }
      },
      "tokenizer": {
        "autocomplete": {
          "type": "edge_ngram",
          "min_gram": 2,
          "max_gram": 10,
          "token_chars": [
            "letter",
            "digits"
          ]
        }
      }
    }
  },
  "mappings":
    {
     "properties":
	    {

	       "RPD_Link":{"type": "text","copy_to": "rpddata"},
	       "RPD#":{"type": "keyword"},
          "Updated_Date":{"type": "keyword"},
	        "Created_Date":{"type": "keyword"},
	         "Type":{"type": "keyword"},
	        "Author":{"type": "text","copy_to": "rpddata"},
	        "Category":{"type": "keyword"},
	        "Severity":{"type": "text","copy_to": "rpddata"},
	        "Assignee":{"type": "text","copy_to": "rpddata"},
	        "Title":{"type": "text","copy_to": "rpddata"},
          "Status":{"type": "keyword"},
	        "Database":{"type": "keyword"},
	        "Group":{"type": "keyword"},
	        "Template":{"type": "text","copy_to": "rpddata"},
          "Query_Type":{"type": "keyword"},
	        "Country":{"type": "text","copy_to": "rpddata"},
	        "Profile":{"type": "keyword"},
	        "Industry_Type":{"type": "keyword"},
          "Question_Type":{"type": "keyword"},
	        "Report_Type":{"type": "text","copy_to": "rpddata"},
	        "Time_Series":{"type": "keyword"},
	        "Year":{"type": "text","copy_to": "rpddata"},
          "Company_Priority":{"type": "keyword"},
	        "SDB_STD_Code":{"type": "text","copy_to": "rpddata"},
	        "Field_Name":{"type": "keyword"},
          "Specific_Account_Name":{"type": "text","copy_to": "rpddata"},
	        "Company_Name":{"type": "text","copy_to": "rpddata"},
	        "PPI":{"type": "keyword"},
          "Memo_definition":{"type": "keyword"},
	        "#Comments":{"type": "keyword"},
	        "rpddata": { "type": "text","analyzer": "autocomplete",
        "search_analyzer": "autocomplete_search"}
	    }
    }
}
res = es.indices.create(index = "rpd32", body = request_body)
print(" response: '%s'" % (res))

