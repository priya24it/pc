from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

doc1 = {"rpd15": "Japanese", "rpddata15": "moderate"}
doc2 = {"food": "Italian", "spice_level": "mild"}
doc3 = {"food": "Indian", "spice_level": "spicy"}
es.index(index="food", doc_type="spice_level", id=1, body=doc1)
resp = es.get(index="food", doc_type="spice_level", id=1)
print("response")
print(resp)

@app.route('/', methods=['GET'])
def index():
    print("response1")
    results = es.get(index='contents', doc_type='title', id='my-new-slug')
    return jsonify(results['_source'])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)