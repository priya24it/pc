from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

es = Elasticsearch()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #results = es.get(index='rpd15', doc_type='rpddata15', id='cFfg9nIBeOApdGnvrA_L')
    results = es.get(index='contents', doc_type='title', id='ab88a22f-d989-4b21-9afc-c9a7cd5eb1cb')
    return jsonify(results['_source'])

@app.route('/index123', methods=['GET'])
def index123():
    #results = es.get(index='rpd15', doc_type='rpddata15', id='cFfg9nIBeOApdGnvrA_L')
    results = es.get(index='contents', doc_type='title', id='ab88a22f-d989-4b21-9afc-c9a7cd5eb1cb')
    return jsonify(results['_source'])

@app.route('/insert', methods=['GET'])
def insert():
    #results = es.get(index='rpd15', doc_type='rpddata15', id='cFfg9nIBeOApdGnvrA_L')
    results = es.get(index='contents', doc_type='title', id='ab88a22f-d989-4b21-9afc-c9a7cd5eb1cb')
    return jsonify(results['_source'])


@app.route('/insert_data', methods=['GET'])
def insert_data():
    print("executed here")

    #slug = request.form['slug']
    #title = request.form['title']
    #content = request.form['content']

    slug = "Priyash1"
    title = "Priyash123"
    content = "Myfather"

    body = {
        'slug': slug,
        'title': title,
        'content': content,
        'timestamp': datetime.now()
    }

    result = es.index(index='contents', doc_type='title', id=slug, body=body)
    return jsonify(result)


@app.route('/search', methods=['GET'])
def search():
    keyword = request.form['keyword']

    body = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["stephen", "title"]
            }
        }
    }

    res = es.search(index="contents", doc_type="title", body=body)
    return jsonify(res['hits']['hits'])

app.run(port=8000, debug=True)