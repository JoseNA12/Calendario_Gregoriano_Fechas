
# R4(fecha): Dada una fecha determinar la cantidad de días que han pasado desde el 1 de Enero del mismo año.

"""
Entradas: "fecha": Lista en forma de tupla con valores enteros positivos que representan una fecha del Calendario Gregoriano
Salidas: Entero: Sumatoria de la cantidad de dias transcurridos entre el 1 de Enero y la fecha indicada. 
Restricciones: El parametro de entrada tiene que ser una lista de 3 elementos, siendo estos numeros enteros positivos
"""

import requerimiento_0
import requerimiento_1
import requerimiento_2

def R4(dias_desde_primero_enero):
    if ((requerimiento_0.R0(dias_desde_primero_enero)) and (requerimiento_2.R2(dias_desde_primero_enero))):
        anio = dias_desde_primero_enero[0]
        mes = dias_desde_primero_enero[1]
        dia = dias_desde_primero_enero[2]
        dias_meses = [31,28,31,30,31,30,31,31,30,31,30,31] #Los dias que posee cada mes en orden de izquierda a derecha
    
        cantidad_dias = 0
        
        for i in range(mes- 1): #Sumar todos los dias desde enero hasta mes anterior
            cantidad_dias += dias_meses[i]
            i += 1
            
        cantidad_dias += dia - 1 #Sumarle la cantidad de dias que han pasado completamente en el mes actual
        
        if(2 < mes and requerimiento_1.R1(anio)): #Si es anio bisiesto y mes mayor a febrero
            cantidad_dias += 1
        
        print(cantidad_dias)
        
    else:
        print("Error en el formato de fecha indicado")

    
        


