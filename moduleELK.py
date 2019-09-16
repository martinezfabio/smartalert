#!/usr/bin/env python
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import moduleParameters as param
from datetime import datetime

# connecta no ELK
def connectElasticSearch():
    ConnectES = Elasticsearch([{'host': param.getHostElasticSearch(), 'port': param.getPortElasticSearch(), 'timeout': 2000}])
    # tenta acessar
    if not ConnectES.ping():
        raise ValueError("Connection failed")
    return ConnectES
	
	
def query_elastic_count(rules):
	es = connectElasticSearch()
	results=es.search(index=param.getIndexElasticSearch(), request_timeout=120, body=
	{
		"size": 0	, 
		"_source": {"includes": [ "message*" ]},
		"query": {
		"bool": {
		"must": [
		{
			"query_string": {
				"query":"( " + rules['queryAtribute'] + ":\"" + rules['queryMessage'] + "\")",
		"analyze_wildcard": True
			}
		},
	{
		"range": {
		"@timestamp": {
						"gte": "now-" + str(rules['queryTime']) + str(rules['queryTypeTime']) + ""
					}
				}
	}
		],
		"must_not": []
				}
			} 
}) 

	v = (results['hits'])
	#print(v['total'])
	
	return v[rules['queryFieldResult']]

