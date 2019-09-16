#!/usr/bin/python
# -*- coding: latin-1 -*-

import moduleELK as elk
import moduleEmail as email
import moduleRule as rule

#Scheduler
import time
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

@tl.job(interval=timedelta(seconds=1000))
def DownloadFaturaZero():
	executaAlerta('DownloadFaturaZero')

def executaAlerta(nomeRegra):
	#carrega parametrização de regras cadastradas no CSV
	rules = rule.loadRules(nameRule = nomeRegra)
	print("Regra selecionada - " + str(rules)+ '\n' + '\n')

	#ELK - Valida quantidade de download de faturas no período
	valueELK = elk.query_elastic_count(rules)
	print("Valor retornado do Elastic - " + str(valueELK)+ '\n' + '\n')

	#Valida se regra do alerta foi atendida 
	alerta = rule.validadeRule(rules, valueELK)
	print("Alerta - " + str(alerta)+ '\n' + '\n')

	#Dispara Email se o alerta for verdadeiro
	if alerta:
		email.SendMail(rules, valueELK)
		print("Email enviado")
		
#-------------------- START ----------------------------------------

if __name__ == "__main__":
	tl.start(block=True)
	