#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
from poo1 import *

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    obbecarios=[]
    for b in becarios:
#        print b
        bec=Becario(b,choice(calificaciones))
#        print bec
        obbecarios.append(bec)
    return obbecarios
#def imprime_calificaciones():
#    for alumno in calificacion_alumno:
#        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

oob=asigna_calificaciones()
for i in oob:
    print i
#imprime_calificaciones()
