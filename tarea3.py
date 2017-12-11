#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
let_num = {'a':'@','e':'3','i':'1','o':'0','s':'5','y':'&'}


def genera_palabras(cad):
    cad = ''.join(map(lambda x:let_num[x] if x in let_num else x,cad))
    return cad

def genera_dicc(entrada,salida):
    dicc = []
    with open(entrada,'r') as lee_archivo, open(salida,'w') as sal_dicc:
        for line in lee_archivo.readlines():
            dicc.append(genera_palabras(line[:-1]))
            print dicc
        
        print dicc
        for passwd in dicc:
            sal_dicc.write('%s\n' % passwd)

genera_dicc('prueba.txt','dicc.txt')
