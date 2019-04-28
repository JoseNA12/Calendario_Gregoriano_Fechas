#dia_inicio_mes(año, mes): Dado un año perteneciente al rango permitido y un mes en el rango válido
#       (1≤mes ≤12), determinar el día de la semana que le correspondeal primer día de ese mesen ese año
#El resultado debe ser un número entero según corresponde en la siguiente codificación:
#   0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado.
"""
Entradas: "(año, mes)": año es un número entero perteneciente a rango permitido y mes debe ser un número entero
                        en el rango válido (1≤mes ≤12).
Salidas: El número del día correspondiente al primer día del mes en el año indicado según los siguientes valores:
         0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado.
Restricciones: El año ingresado debe de ser mayor a 1582, que es cuando se empieza a utilizar el calendario Gregoriano
               El mes ingresado debe petenecer al rango permitido (1≤mes ≤12).
"""
import requerimiento_1
import requerimiento_5

def dia_inicio_mes (año, mes):
    if(isinstance(año,int) and isinstance(mes,int)):  #Se valida que las entradas sean números enteros
        if(año>1582):                                 #Se valida que el año pertenezca al calendario Gregoriano(año>1582)
            if(mes>0 and mes<13):                     #Se valida que el mes pertenezca al rango válido (1≤ mes ≤12)
                retorno = requerimiento_5.calcularDoomsday((año,mes,1)) #Se calcula el primer día del mes en el año indicado y se almacena en una variable a ser retornada
                if(requerimiento_1.R1(año)):          #Si es año bisiesto se resta uno al resultado
                    if retorno == 0:                   #Si es año bisiesto y "retorno=0" retorna el 6 para indicar que es sábado
                        return 6
                    else:                             #Si es año bisiesto y "retorno!=0" se resta 1 a la variable "retorno"
                        retorno-=1
                return retorno
            else:
                return "El mes ingresado debe pertenecer al rango válido (1≤ mes ≤12)"
        else:
            return "El año no pertenece al claendario Gregoriano. Debe ser mayor a 1582"
    else:
        return "Los datos ingresados deben ser números enteros"
