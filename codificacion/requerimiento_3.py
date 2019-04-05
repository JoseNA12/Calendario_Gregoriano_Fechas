# R3(fecha_es_valida): Dada una fecha, determinar la fecha del día siguiente.
# El resultado debe ser una fecha válida.

import requerimiento_1
import requerimiento_2

"""
Entradas: "dia_siguiente": es una fecha válida en forma de tupla.
Salidas: La fecha correspondiente al día siguiente de la entrada.
Restricciones: Si es el útlimo día del último mes, aumentar el año.
               Si es el último día del mes, aumentar el mes.
               Si no es el último día del mes, amuentar el día.
"""

def R3(dia_siguiente):
    anio = dia_siguiente[0]
    mes = dia_siguiente[1]
    dia = dia_siguiente[2]
    dias_meses = [31,28,31,30,31,30,31,31,30,31,30,31] #Los días que posee cada mes en orden de izquierda a derecha
    if(requerimiento_2.R2(dia_siguiente)): # Se valida que sea una fecha válida
        if(requerimiento_1.R1(anio)): #Si es año bisiesto se cambia la cantidad de días de Febrero en la lista
            dias_meses[1]+=1
        if(dia != dias_meses[mes-1]):
            return (anio, mes, dia+1)       #Si el día no es el último del mes
        else:
            if(mes == 12):
                return (anio+1, 1, 1)   #Si es el último día del mes de diciembre
            else:
                return (anio, mes+1, 1) #Si es el último día del mes que no sea Febrero ni Diciembre
    else:
        return "No es una fecha válida"
        

