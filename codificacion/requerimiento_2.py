# R2(fecha_es_valida): Dada una fecha, determinar si ésta es válida.
# El resultado debe ser un valor booleano, True o False.

import requerimiento_1

"""
Entradas: "fecha_es_valida": lista en forma de tupla, con valores enteros positivos
Salidas: True si la fecha es correcta, segun sus dias respecto al mes y al año. False si no es valida
Restricciones: El formato de la tupla es (año, mes, día), donde contiene valores enteros positivos.
               El dia maximo debe ser acorde al mes y año (si es bisiesto o no). El mes debe ser un
               valor entre 1 y 12.
"""

def R2(fecha_es_valida):    # Se asume el formato: (año, mes, día)
    meses_dict = {	    # Diccionario con los meses y la cantidad dias respectivamente
        "enero": 31,
        "febrero": 28,
        "marzo": 31,
        "abril": 30,
        "mayo": 31,
        "junio": 30,
        "julio": 31,
        "agosto": 31,
        "septiembre": 30,
        "octubre": 31,
        "noviembre": 30,
        "diciembre": 31
    }

    anio = fecha_es_valida[0]   # Asignacion de los valores de la tupla en variables
    mes = fecha_es_valida[1]
    dia = fecha_es_valida[2]

    if (requerimiento_1.R1(anio)):  # Comprobar si el año es bisiesto, si sucede
        meses_dict["febrero"] = meses_dict.get("febrero") + 1		    # .. se suma +1 dia al mes de febrero

    if ((mes < 1) or (mes > 12)):		                            # Verificar que el mes ingresado esté entre 1 y 12
        return False

    if ((dia < 1) or (dia > list(meses_dict.values())[mes - 1])):	    # Verificar que los dias ingresados sean acorde al mes,
        return False                                                        # .. se pasa el diccionario de meses en forma lista conteniendo
                                                                            # .. los valores (cantidad de días), luego se obtiene por medio
    return True                                                             # .. de un indice el valor respectivo acorde al mes ingresado
