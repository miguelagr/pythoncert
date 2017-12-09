#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def palindromo(palabra):
    ppalabra=""
    for i in palabra.split():
        ppalabra += i.upper()
    if ppalabra == ppalabra[::-1]:
        return True
    return False

palindromo("anita lava la tina")
#print becarios
