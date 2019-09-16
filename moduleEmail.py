#!/usr/bin/env python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart






def SendMail(rules, valueELK):
	msg = MIMEMultipart()
	msg['Subject'] = rules['subjectMail']
	msg['From'] = 'smartalert@gmail.com'
	recipients = list(rules['listMail'].split(","))
	msg['To'] = ", ".join(recipients)
	

	text = MIMEText("Nas ultimas " + rules['queryTime'] + " horas tivemos os seguintes indicadores para " + rules['nameFunction'] + '\n' + '\n'  )
	text1 = MIMEText(rules['bodyEmailMessageErro'] + " :  - " + str(valueELK) + ' qtd' + '\n' + '\n')
	text2 = MIMEText(rules['bodyEmailMessageInfo'] + '\n' + '\n')
	
	link  = MIMEText(u'<a href="' + rules['bodyEmailLink'] + '">Report Kibana</a>','html')

	msg.attach(text)
	msg.attach(text1)
	msg.attach(text2)
	msg.attach(link)
	
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login('smartalert@gmail.com', 'smartalert*&%')
	s.sendmail('smartalert@gmail.com', recipients, msg.as_string())
	s.quit()