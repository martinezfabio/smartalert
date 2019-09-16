#!/usr/bin/env python
import datetime
import moduleParameters as param
import csv



def loadRules(nameRule):
	with open(param.getPathRule()) as fh:
		dict  = csv.DictReader(fh, delimiter=';') 
		
		for row in dict:
			if row['nameRule'] == nameRule:
				return row

				
def validadeRule(rules, valueELK):
	if rules['typeRule'] == 'IGUAL':
		return str(valueELK) == rules['valueRuleFinal']
		
	if rules['typeRule'] == 'MAIOR':
		return str(valueELK) > rules['valueRuleFinal']
		
	if rules['typeRule'] == 'MENOR':
		return str(valueELK) < rules['valueRuleFinal']

