from random import *

def passwd(minusculas,mayusculas,digitos,contra=""):
    chars=[]
    if minusculas:
        chars.append("min")

    if mayusculas:
        chars.append("may")

    if digitos:
        chars.append("dig")

    if chars:
        agrega = choice(chars)

        if agrega == "min":
            contra = contra + chr(randint(ord('a'),ord('z')))
            return passwd(minusculas-1,mayusculas,digitos,contra)
        elif agrega == "may":
            contra = contra + chr(randint(ord('A'),ord('Z')))
            return passwd(minusculas,mayusculas-1,digitos,contra)
        elif agrega == "dig":
            contra = contra + chr(randint(ord('0'),ord('9')))
            return passwd(minusculas,mayusculas,digitos-1,contra)

    return contra
