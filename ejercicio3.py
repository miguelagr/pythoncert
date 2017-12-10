#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

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
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def aprobados_reprobados():
    asigna_calificaciones()
    aprobados = []
    reprobados = []
    for b in calificacion_alumno:
        if calificacion_alumno[b] >= 8:
            aprobados.append(b)
        else:
            reprobados.append(b)
    return tuple(aprobados),tuple(reprobados)

def promedio():
    prom = 0.0
    i = 0
    for b in calificacion_alumno:
        prom += calificacion_alumno[b]
        i += 1
    if i:
        prom = prom/i
    return prom

def conjunto():
    con = []
    for b in calificacion_alumno:
        con.append(calificacion_alumno[b])

    return set(con)

print aprobados_reprobados()
print promedio()
print conjunto()
