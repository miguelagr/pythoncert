#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT


def maximo_palindromo(cadenar):
    cadena=""
    for c in cadenar.split():
        cadena += c
    #print cadena
    
    maxp=""
    pal=""
    for i in range(len(cadena)):
        for j in range(len(cadena))[::-1]:
            if cadena[i:j] + cadena[j] == cadena[j:i:-1] + cadena[i]:
                pal = cadena[i:j]+cadena[j]
                break
        if len(pal) > len(maxp):
            maxp = pal

    print maxp

maximo_palindromo("aaanitalaval atinaaa aaaaaaaaaaaa")
