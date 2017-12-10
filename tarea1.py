#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def maximo_palindromo(cadenar):
    """
    Regresa el palìndromo mas grande
    que puede ser formado
    Recibe:
        str - La cadena de la que extraemos el palindromo mas grande
    Regresa:
        str - El palindromo mas grande encontrado
    """
    cadena=""
    for c in cadenar.split():
        cadena += c
    maxp=""
    pal=""
    for i in range(len(cadena)):
        for j in range(len(cadena))[::-1]:
            if cadena[i:j] + cadena[j] == cadena[j:i:-1] + cadena[i]:
                pal = cadena[i:j]+cadena[j]
                break
        if len(pal) > len(maxp):
            maxp = pal
    return maxp

print maximo_palindromo("aaanitalaval atinaaa aaaaaaaaaaaa")
