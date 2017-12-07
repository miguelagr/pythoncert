#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

aprobados = []



def palindromo(palabra):
    ppalabra=""
    palabras = palabra.split()
    for i in palabras:
        ppalabra += i
    print ppalabra
    print ppalabra[::-1]
    if ppalabra == ppalabra[::-1]:
        print "si es"
        return True
    return False

palindromo("anita lava la tina")
#print becarios
