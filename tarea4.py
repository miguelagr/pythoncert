#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import xml.etree.ElementTree as ET

def cuenta_hosts(hosts):
	prendidos = filter(lambda x: x.find('status').get('state') == 'up', hosts)
	apagados =  filter(lambda x: x.find('status').get('state') == 'down', hosts)	
	print len(prendidos)
	print len(apagados)

def crea_arbol(archivo):
	with open(archivo,'r') as xmlraw:
		xmlp = ET.fromstring(xmlraw.read())
		hosts = xmlp.findall('host')
		print len(hosts)
		cuenta_hosts(hosts)
crea_arbol('nmap.xml')
