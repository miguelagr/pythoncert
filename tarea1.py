#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

from math import *

def maximo_palindromo(cadenar):
    """
    Regresa el palìndromo mas grande
    que puede ser formado
    Argumentos:
        cadena (str)
    Salida:
        palindromo (str)
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

def num_primo(n):
    """
    Regresa en valor booleano si es primo o no
    Argumentos:
        numero (int)
    Salida:
        Cierto o falso (bool)
    """
    for i in range(int(sqrt(n))+1):
        if i not in range(2):
            if n % i == 0:
                return False
    return True

def list_primos(n,i=2,primos=[]):
    """
    Regresa en valor booleano si es primo o no
    Argumentos:
        tamaño de la lista (int)
    Salida:
        lista de numeros (int[])
    """
    if n<0:
        return primos
    else:
        if num_primo(i):
            primos.append(i)
            n -= 1
        return list_primos(n,i+1,primos)

print list_primos(10)
print maximo_palindromo("aaanitalaval atinaaa aaaaaaaaaaaa")
