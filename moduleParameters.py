#!/usr/bin/env python
import datetime


# funcao que retorna o host do ELK
def getHostElasticSearch():
	return 'elastic'

# funcao que retorna a porta do ELK
def getPortElasticSearch():
    return '9200'

# funcao que retorna o index do ELK
def getIndexElasticSearch():
	#data = datetime.datetime.now().strftime("%d%m%Y")
	#return 'logstash-**' + str(data)
	return 'logstash-**'

	
def getPathRule():
	return "C:\\D\\CIT\\Vivo\\python\\alerta\\rules.csv"