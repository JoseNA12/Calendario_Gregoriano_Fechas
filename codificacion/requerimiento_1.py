# R1(bisiesto): Dado un año perteneciente al rango permitido, determinar si este es bisiesto.
# El resultado debe ser un valor booleano, True o False

"""
Entradas: "bisiesto": numero entero
Salidas: Booleano: True si el año ingresado es bisiesto. False si no es bisiesto 
Restricciones: El parametro de entrada tiene que ser un numero entero
"""

def R1(bisiesto):
    if (type(bisiesto) is int):								   # Comprobar que el año ingresado sea número entero
        if (((bisiesto % 4) == 0) and ((bisiesto % 100) != 0)) or ((bisiesto % 400) == 0): # Un año es bisiesto si:
            return True									   # .. es divisible entre 4 y no entre 100
        else:
            return False
    else:
        return False

