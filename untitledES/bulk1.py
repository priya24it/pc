#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from elasticsearch import Elasticsearch, helpers
import os, uuid

elastic = Elasticsearch("http://localhost:9200")
actions = ''' {"index":{"_index":"employees","_id":0}} {"type":"act","line_id":1,"play_name":"Henry IV", "speech_number":"","line_number":"","speaker":"","text_entry":"ACT I"} '''
print(actions)
response = helpers.bulk(elastic, actions, index='employees', doc_type='people')
print("\nactions RESPONSE:", response)