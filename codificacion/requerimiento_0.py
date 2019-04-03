# R0(fecha_es_tupla): Todas las fechas serán creadas como tuplas de tres números enteros positivos (ternas),
# en este orden: (año, mes, día). El resultado debe ser un valor booleano, True o False.

"""
Entradas: "fecha_es_tupla": lista en forma de tupla con valores enteros positivos
Salidas: Booleano: True si la tupla es valida. False si la tupla no es valida
Restricciones: El parametro de entrada tiene que ser una lista de 3 elementos, siendo estos numeros enteros positivos
"""
def R0(fecha_es_tupla):
    if (len(fecha_es_tupla) == 3): 		    # Verificar que la longitud de la tupla sea la correcta
        for i in range(0, 3):			    # Iterar en un rango de 0 a 2 sobre la tupla para accesar los valores
            if (type(fecha_es_tupla[i]) is int):    # Comprobar que los elementos de la tupla sean números enteros
                if (fecha_es_tupla[i] < 1):	    # Comprobar que los elementos de la tupla sean números positivos
                    return False
            else:
                return False
    else:
        return False
    return True	
