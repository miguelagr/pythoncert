#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import re
import sys
import argparse
from requests import get
from requests.exceptions import ConnectionError
import requests

def addOptions():
    """

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose', dest='verbose', default=None, action='store_true', help='Mostrar los detalles de ejecucion en tiempo real')
    parser.add_argument('-T','--tor',dest='tor',default=None,action='store_true',help='Bandera que habilita el uso de tor') 
    parser.add_argument('-r','--report',dest='report',default='report.txt',help='Archivo de reporte')
    parser.add_argument('-H','--cabeceras',dest='headers',default=False,action='store_true',help='Habilitar el analisi de cabeceras')
    parser.add_argument('-M','--metodos',dest='methods',default=False,action='store_true',help='Habilita la deteccion de metodos')
    parser.add_argument('-C','--correos',dest='mails',default=False,action='store_true',help='Habilita la extraccion de correos')
    parser.add_argument('-P','--protocol',dest='protocol',default='http',help='Especifica protocolo')
    parser.add_argument('-p','--port', dest='port', default=None, help='Puerto.')
    parser.add_argument('-s','--server', dest='server', default=None, help='Indica el servidor.')
    parser.add_argument('-F','--files', dest='files', default=None, help='Archivo de recursos de busqueda.')
    args = parser.parse_args()
    return args
 

def crea_urlr(url,doc):
    """
    Crea una URL de los recursos de busqueda
    Argumentos:
        url (str) : La url del servidor
        doc (str) : el recurso del servidor
    Salida:
        urlr (str) : la url del recurso
    """
    urlr = '%s/%s' % (url,doc)
    return urlr

def analiza_recursos(url,archivo,verboso = False):
    """
    Escanea el servidor en busca de recursos vulnerables
    Argumentos:
        archivo (url) : El nombre del archivo que contiene la lista de recursos
    Salida:
        urls_vulnerables (url)[] : Una lista de urls con recursos vulnerables
    """
    urls_vulnerables=[]
    with open(archivo,'r') as arcs:
        ars = [ar[:-1] for ar in arcs.readlines()]

    urls = [crea_urlr(url,urlr) for urlr in ars]
    if verboso:
        print "Numero de recursos a analizar:"
        print len(urls)

    for i in urls:
        if verboso:
            print "Analizando recurso:"
            print i
        try:
            ri = requests.get(i)
        except Exception as e:
            printError(e,True)
        historia = map(lambda x: x.status_code,ri.history)
        if ri.status_code == 200 and 302 not in historia:
            if verboso:
                print "Recuso encontrado"
            urls_vulnerables.append(i)
        if verboso:
            print '\n'

    return urls_vulnerables



def crea_url(servidor,puerto,protocolo='http'):
    """
    Regresa la URL formada por los argumentos de entrada
    Argumentos:
        servidor (str) : El DNS o IPv4 del servidor web
        puerto (str) : El puerto del servidor
        protocolo (str) : Protocolo de transferencia de hipertexto
    Salida:
        url (str) : La URL formada
    """
    if puerto:
        puerto = ':%s' % puerto
        url = '%s://%s%s' % (protocolo,servidor,puerto)
    else:
        url = '%s://%s' % (protocolo,servidor)
    return url

def crea_sesion(tor=False):
    """
    Crea una objeto sesion
    Argumentos:
        tor (bool) : verdadero para usar tor como proxy
    Salida:
        sesion (session) : Un objeto session de la libreria requests
    """
    sesion = requests.session()
    if tor:
        sesion.proxies = {'http':'socks5://127.0.0.1:9050','https':'socks5://127.0.0.1:9050'}
    return sesion

def analiza_cabeceras(url,sesion):
    """
    Analiza las cabeceras recibidas del metodo HEAD al servidor
    Argumentos:
        url (str) : La URL del servidor
        sesion (session) : objeto session
    Salida:
        servidor (str) : La version del servidor
        php (str) : La version PHP que utiliza el servidor
    """
    try:
        respuesta = sesion.head(url)
    except Exception as e:
        printError('Error de conexion')
        printError(e,True)


    try:
        servidor = respuesta.headers['Server']
    except Exception as e:
        servidor = 'Version del servidor oculta'

    try:
        php = respuesta.headers['X-Powered-By']
    except Exception as e:
        php = 'Version PHP oculta'

    return servidor,php

def analiza_cuerpo(url,sesion):
    """
    Analiza las cabeceras recibidas del metodo HEAD al servidor
    Argumentos:
        url (str) : La URL del servidor
        sesion (session) : objeto session
    Salida:
        cms (str) : El CMS utilizado por la pagina
        correos (str)[] : Lista de correos encontrados en la pagina
    """
 
    try:
        respuesta = sesion.get(url)
    except Exception as e:
        printError(e,True)
    try:
        cms = re.findall('<[^<]+generator[^>]+>',respuesta.content)
        if len(cms) > 0:
            cms = re.findall('content=".+"',cms[0])
            if len(cms) > 0:
                cms = re.findall('[^"]+',re.findall('".+"',cms[0])[0])[0]

        correos = re.findall('[a-zA-Z0-9]+@.+\.[a-zA-Z]+',respuesta.content)
        return cms,correos
    except Exception as e:
        print 'No se encontro nada en el cuerpo de la pagina'

def analiza_metodos(url,sesion):
    """
    Analiza las cabeceras recibidas del metodo HEAD al servidor
    Argumentos:
        url (str) : La URL del servidor
        sesion (session) : objeto session
    Salida:
        servidor (str) : La version del servidor
        php (str) : La version PHP que utiliza el servidor
    """
    try:
        respuesta = sesion.options(url)
    except Exception as e:
        metodos = 'Se deshabilito deteccion de metodos'

    try:
        metodos = respuesta.headers['Allow']
    except Exception as e:
        metodos = 'Se desactivo la deteccion de metodos'
    return metodos

def printError(msg, exit = False):
    """
    Funcion para escapar de la ejecucion del programa
    Argumentos:
        msg (str) : Mensaje de error
        exit (bool) : Verdadero escapa del programa, falso continua ejecucion
    Salidas:
        Ninguna
    """
    sys.stderr.write('Error:\t%s\n' % msg)
    if exit:
        sys.exit(1)

if __name__ == '__main__':
    """
    Este programa requiere la instalacion del servicio Tor, la libreria requests, y el protocolo
    SOCKS.

    """
    try:
        opts = addOptions()
        if not opts.server:
            printError('No se ha indicado servidor',True)
        url = crea_url(opts.server,opts.port,opts.protocol)
        #sesion = crea_sesion(opts.tor)
        servidor,php = analiza_cabeceras(url,crea_sesion(opts.tor))
        metodos = analiza_metodos(url,crea_sesion(opts.tor))
        cms,correos = analiza_cuerpo(url,crea_sesion(opts.tor))
        urls_vulnerables = []
        if opts.files:
            urls_vulnerables = analiza_recursos(url,opts.files,opts.verbose)

        if opts.verbose:
            if opts.headers:
                print "Version del servidor web:"
                print servidor
                print "\n"
                print "Version PHP:"
                print php
                print "\n"
            if opts.methods:
                print "Metodos habilitados:"
                print metodos
                print "\n"

            if len(cms) == 0 and opts.headers:
                print "No se ha encontrado generador de recursos"
                print "\n"
            elif opts.headers:
                print "CMS encontrado:"
                print cms
                print "\n"
            if len(correos) == 0 and opts.mails:
                print "No se han encontrado correos"
                print "\n"
            elif opts.mails:
                print "Correos encontrados:"
                for i in correos:
                    print i

            if opts.files and len(urls_vulnerables) == 0:
                print "no se encontraron recursos vulnerables"
            elif len(urls_vulnerables) > 0:
                print "Se encontraron los siguientes recursos vulnerables"
                for i in urls_vulnerables:
                    print i

            #import async requests
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
