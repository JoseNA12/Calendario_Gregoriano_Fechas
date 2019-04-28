# fecha_futura(tupla,dias):  Dada una fecha válida f y un número entero no-negativo n, determinar
# la fecha que está n días naturales en el futuro. El resultado debe ser una fecha válida.

import requerimiento_0
import requerimiento_1
import requerimiento_2

"""
Entradas: "tupla": Lista en forma de tupla, con valores enteros positivos que representa una fecha del Calendario Gregoriano.
          "dias": Cantidad de días que se desea aumentar la fecha indicada.
Salidas:  False si la fecha indicada no es valida.
          Tupla que representa la fecha luego del incremento de días.
Restricciones: El formato de la tupla es (año, mes, día), donde contiene valores enteros positivos.
               El dia maximo debe ser acorde al mes y año (si es bisiesto o no). El mes debe ser un
               valor entre 1 y 12.
               El valor de dias ingresado debe ser un entero positivo
"""

def fecha_futura(tupla,dias):    # Se asume el formato: (año, mes, día)
    dias_meses = [31,28,31,30,31,30,31,31,30,31,30,31] #Los días que posee cada mes en orden de izquierda a derecha
    anioTupla = tupla[0]
    mesTupla = tupla[1]
    diaTupla = tupla[2]
    if(requerimiento_0.R0(tupla)): #Validar la tupla ingresada
        if(requerimiento_2.R2(tupla)): # Se valida que sea una fecha válida
            if ((type(dias) is int) and dias > 0): # Validar que sea un número natural positivo
                if(requerimiento_1.R1(anioTupla)): #Si es año bisiesto se cambia la cantidad de días de Febrero en la lista
                    dias_meses[1]+=1
                if(diaTupla <= dias_meses[mesTupla-1]-dias):
                    return (anioTupla, mesTupla, diaTupla+dias)       #Si el día no es el último del mes
                else: 
                    diaNuevo = diaTupla + dias #Dia incrementado para la nueva fecha
                    indiceMes = mesTupla-1 # Mes actual
                    anioNuevo = anioTupla # Año actual
                    while(diaNuevo > dias_meses[indiceMes]): 
                        diaNuevo -= dias_meses[indiceMes] # Restar los días de cada mes
                        indiceMes += 1 
                        if(indiceMes == 12):
                            indiceMes = 0
                            anioNuevo += 1
                    if(mesTupla == 12):
                        return (anioNuevo, indiceMes+1, diaNuevo)   #Si es el último día del mes de diciembre
                    else:
                        return (anioNuevo, indiceMes+1, diaNuevo) #Si es el último día del mes que no sea Febrero ni Diciembre
            else:
                return "La cantidad de días debe ser un número natural positivo"
        else:
            return "No es una fecha válida"
    else:
        return "No es una fecha válida"



fecha_futura((2019,4,28),5)
fecha_futura((2019,12,31),365)
fecha_futura((2019,4,28),5)
fecha_futura((2019,4,28),5)

