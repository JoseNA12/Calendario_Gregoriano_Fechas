# R3(fecha_es_valida): Dada una fecha, determinar la fecha del día siguiente.
# El resultado debe ser una fecha válida.

import requerimiento_1

def R3(dia_siguiente):
    anio = dia_siguiente[0]
    mes = dia_siguiente[1]
    dia = dia_siguiente[2]
    dias_meses = [31,28,31,30,31,30,31,31,30,31,30,31] #Los días que posee cada mes en orden de izquierda a derecha
    if(dia != dias_meses[mes-1]):
        return (anio, mes, dia+1)       #Si el día no es el último del mes
    else:
        if(mes == 2 and requerimiento_1.R1(anio)):
            return (anio, mes, dia+1) #Si el mes es febrero y el año es bisiesto
        elif(mes == 12):
            return (anio+1, 1, 1)   #Si es el último día del mes de diciembre
        else:
            return (anio, mes+1, 1) #Si es el último día del mes que no sea Febrero ni Diciembre
        

