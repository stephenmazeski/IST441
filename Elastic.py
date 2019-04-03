import json

from elasticsearch import Elasticsearch

# GLOB HERE
file_name = 'data.jl'

# ElasticSearch Object
# team change port in the following line - 9 2 0 _ - Eg. Team04 has port 9204
es = Elasticsearch([{'host': 'localhost', 'port': 9208}])

# list of json objects
data = []

with open(file_name) as f:
    for line in f:
        data.append(json.loads(line))

# index each json
idx = 0
index_name = 'jian_urls'

for body in data:
    try:
        es.index(index=index_name, doc_type='doc', id=idx, body=body)
    except:
        continue
    idx += 1
