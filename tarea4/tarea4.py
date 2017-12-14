#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import xml.etree.ElementTree as ET
import matplotlib.pyplot as pyt
from datetime import datetime
import hashlib

def printError(msg, exit = False):
    """
    Funcion para salir en caso de erro
    Argumentos:
        Mensaje de error (str)
    Salida:
        Valor para indicar la salida de ejecucion (bool)
    """
    sys.stderr.write('Error:\t%s\n' % msg)
    if exit:
        sys.exit(1)

def genera_hashes(archivo):
    smd5 = hashlib.md5()
    ssha1 = hashlib.sha1()
    arr = open(archivo,'r')
    smd5.update(arr.read())
    arr = open(archivo,'r')
    ssha1.update(arr.read())
    return smd5.hexdigest(),ssha1.hexdigest()

def hosts_prendidos(hosts):
    """
    Indica numero de hosts prendidos
    Argumentos:
        hosts (ElementTree)
    Salida
        Hosts prendidos (ElementTree)
    """
    prendidos = filter(lambda x: x.find('status').get('state') == 'up', hosts)
    return prendidos

def genera_csv(host,salidacsv):
    """
    Genera archivo csv
    Argumentos:
        Host (ElementTree)
        Nombre del archivo csv (str)
    Salida:
        Ninguna
    """
    with open(salidacsv,'a+') as arcsv:
        arcsv.write('%s,%s' % (host.find('address').get('addr'),host.find('status').get('state')))

def crea_arbol(archivo,salidar,salidacsv):
    """
    Crea estructuras ElementTree a partir del 
    archivo de entrada
    Argumentos:
        Nombre del archivo de entrada (str)
        Nombre del archivo csv (str)
    Salidas:
        Ninguna
    """
    smd,ssha = genera_hashes(archivo)
    salcsv = open(salidacsv,'w')
    salcsv.write('IPv4,Estado,Puerto22,EsHoney,NombreDom\n')
    salcsv.close()
    with open(archivo,'r') as xmlraw, open(salidar,'w') as repo:
	xmlp = ET.fromstring(xmlraw.read())
	hosts = xmlp.findall('host')
        prendidos = hosts_prendidos(hosts)
        for host in hosts:
            genera_csv(host,salidacsv)
        
        repo.write('%s\n' % datetime.now().strftime('%d/%m/%y - %H:%M:%S'))
        repo.write('md5: %s \nsha1: %s\n' % (smd,ssha))
        repo.write('Hosts totales: %s\n' % len(hosts))
        repo.write('Hosts prendidos: %s\n' % len(prendidos))
        repo.write('Hosts Apagados: %s\n' % (len(hosts)-len(prendidos)))
        
        print "Fecha y hora:"
        print datetime.now().strftime('%d/%m/%y - %H:%M:%S')
        print "sha1"
        print ssha
        print "md5"
        print smd
        print "hosts totales"
        print len(hosts)
        print "hosts prendidos"
        print len(prendidos)
        print "hosts apagados"
        print (len(hosts)-len(prendidos))

        etiq = 'Prendidos' , 'apagados'
        tam = [((len(prendidos)*100)/len(hosts)),(100-(len(prendidos)*100)/len(hosts))]
        pyt.pie(tam,labels=etiq)
        pyt.axis('equal')
        pyt.show()
        

if __name__ == '__main__':
    """
    Modo de uso
    ./tarea4 "Archivo de entrada" "Archivo de salida" "Archivo csv"
    """
    if len(sys.argv) != 4:
        printError('Indicar archivo a leer, archivo de reporte y archivo csv .', True)
    else:
        crea_arbol(sys.argv[1],sys.argv[2],sys.argv[3])
