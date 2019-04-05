# R5(anio): Dado un año, indicar cual día de la semana es el primero de Enero
# El resultado debe ser un número entero según del día de la semana.
# 0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado.

import requerimiento_1

"""
Entradas: "dia_primero_enero": es un año del cual se quiere saber el día que fue primero de Enero.
Salidas: El número del día correspondiente según los siguientes valores:
         0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado.
Restricciones: El año ingresado debe de ser mayor a 1582, que es cuando se empieza a utilizar el calendario Gregoriano.
"""

def R5(dia_primero_enero):
    if(dia_primero_enero>1582):    
        return calcularDoomsday((dia_primero_enero,1,1))
    else:
        return "El año no pertenece al claendario Gregoriano."


def calcularDoomsday(fecha):
    TablaMeses = [0,3,3,6,1,4,6,2,5,0,3,5]                                      #Valores según cada mes necesarios para la fórmula
    TablaSiglos = [6,4,2,0]                                                     #Valores según cada siglo necesarios para la fórmula
    PrimeraTabla = [0,3,4,0,1,4,5,0,2,5]                                        #Valores necesarios para la fórmula
    SegundaTabla = [0,1,2,3,5,6,0,1,3,4,5,6]                                    #Valores necesarios para la fórmula
    siglo = fecha[0]//100
    PrimerDigitoAnio = (fecha[0]%100 - fecha[0]%10)//10                         #Primer digito del año sin contar los primeros 2
    SegundoDigitoAnio = (fecha[0]%10)                                           #Segundo dígito del año sin contar los primeros 2
    if(fecha[1]==1 or fecha[1]==2):
        if(requerimiento_1.R1(fecha[0])):                                       #Si es año bisiesto se utiliza un -1 en la fórmula
            TablaMeses[0]-=1
    if (esPar(PrimerDigitoAnio)==False):                                        #Si PrimerDigitoAnio es impar, se suma 2 al SegundoDigitoAnio
        SegundoDigitoAnio+=2
    return (fecha[2]+TablaMeses[fecha[1]-1]+(TablaSiglos[siglo%4])+PrimeraTabla[PrimerDigitoAnio]+SegundaTabla[SegundoDigitoAnio])%7 #Formula utilizada



def esPar(num):     #Función para verificar si un número es par
    if(num%2==0):
        return True
    return False








