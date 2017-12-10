#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas




print (lambda lst1,lst2,lst3,lst4:map(lambda x: x.upper(),filter(lambda x:'i' in x, lst1+lst2+lst3+lst4)))(sistemas,op_interna,incidentes,auditorias)


# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"


# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION

print (lambda lst1,lst2,lst3,lst4:','.join(map(lambda x: x.upper(),filter(lambda x:'i' in x, lst1+lst2+lst3+lst4))))(sistemas,op_interna,incidentes,auditorias)


#funcion que agregue a una sola cadena unido por una coma
