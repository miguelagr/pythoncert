#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from itertools import *
let_num = {'a':'4','e':'3','i':'1','o':'0','s':'5','y':'&'}


def may_min(cad):
    with open('dicc.txt','a+') as sal_dicc:
        for i in range(len(cad)+1)[1:]:
            for comb in combinations(range(len(cad)),i):
                li=list(cad)
                for ind in comb:
                    li[ind]=li[ind].upper()
                sal_dicc.write('%s\n' % ''.join(li))
        sal_dicc.close()


def genera_palabras(cad):
    cad = ''.join(map(lambda x:let_num[x] if x in let_num else x,cad))
    return cad

def genera_dicc(entrada):
    dicc = []
    dicci = dicc
    with open(entrada,'r') as lee_archivo:
        for line in lee_archivo.readlines():
            dicc.append(line[:-1])
        for palp in permutations(dicci,2):
            dicc.append(''.join(palp))

        print dicc
        for pal in dicc:
            print pal
            may_min(pal)
genera_dicc('prueba.txt')
