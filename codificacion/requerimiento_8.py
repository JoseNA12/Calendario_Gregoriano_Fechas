# R8(dias_entre): Dadas dos fechas válidas, f1 y f2, sin importar si f1 ≤ f2 o f2 ≤ f1, 
# determinar el número de días naturales entre las dos fechas. Si f1 = f2, 
# entonces días_entre(f1, f2) = 0.El resultado debe ser un número entero no negativo.

"""
Entradas: "f1": tupla con números enteros no negativos.
          "f2": tupla con números enteros no negativos.
Salidas: Un número entero no negativo.
Restricciones: "f1" y "f2" deben ser tuplas teniendo la tener la forma (año, mes, día), donde contiene valores enteros positivos.
               El dia maximo debe ser acorde al mes y año (si es bisiesto o no). El mes debe ser un
               valor entre 1 y 12.
"""

import requerimiento_0
import requerimiento_1
import requerimiento_2

def dias_entre(f1, f2):
    if ((requerimiento_0.R0(f1) == True) and (requerimiento_0.R0(f2) == True)): # verificar el formato de las fechas
        if ((requerimiento_2.R2(f1) == True) and (requerimiento_2.R2(f2) == True)): # se comprueba de acuerdo al calendario gregoriano, el mes y los dias respectivos
            if (f1EsFechaMenor(f1, f2) != True): # si f1 no es menor, pasa a ser la menor 
                temp = f2
                f2 = f1
                f1 = temp

            dias_meses = [31,28,31,30,31,30,31,31,30,31,30,31] # días de cada mes, en orden de izquierda a derecha
            diasTranscurridos = 0
            nuevoF1 = list(f1)  # convertir las tuplas en listas para editar valores
            nuevoF2 = list(f2)
            banderaBisiesto = False # validar el incremento del mes febrero en los años bisiestos cada 4 años
            
            while (sonFechasIguales(nuevoF1, nuevoF2) != True): # la idea es hacer f1 la misma fecha que f2
                if ((nuevoF1[2] - 1) == dias_meses[nuevoF1[1] - 1]): # si estoy en el ultimo dia - 1 del mes 
                    nuevoF1[2] = 1                             # el dia inicia en 1

                    if (nuevoF1[1] < 12):                      # si no estoy en el numero de mes maximo
                        nuevoF1[1] += 1                        # se incrementa el mes en 1
                    else:
                        nuevoF1[1] = 1                         # pero si estoy en el mes 12
                        nuevoF1[0] += 1                        # el mes empezará en 1

                        if (requerimiento_1.R1(nuevoF1[0]) == True): # si es año bisiesto se suma 1 al mes de febrero
                            dias_meses[1] += 1
                            banderaBisiesto = True             # el año siguiente disminuye 1 dia a febrero.
                        elif (banderaBisiesto != False):       # *Solo entra al condicional cuando un año atras hubo un bisiesto
                            dias_meses[1] -= 1                 
                            banderaBisiesto = False                
                nuevoF1[2] += 1                                # se incrementa el dia en + 1
                diasTranscurridos += 1                         # cuenta global de los dias transcurridos
            return diasTranscurridos
        else:
            print("Alguna fecha presenta valores incorrectos de acuerdo al calendario gregoriano")
    else:
        print("Alguna fecha presenta un error de formato")

# Determinar si dos tuplas contienen los mismos digitos en el mismo orden
def sonFechasIguales(f1, f2):
    for x in range(0, 3): # longitud de tres digitos, tupla
        if (f1[x] != f2[x]): # si algun digito es diferente, falso
            return False
    return True

# Determinar si f1 es una fecha menor a f2
def f1EsFechaMenor(f1, f2):
    if (f1[0] == f2[0]):        # si los años son iguales comparo el mes
        if (f1[1] == f2[1]):    # si los meses son iguales comparo los dias
            if (f1[2] < f2[2]): # es True si los dias de f1 son menores a los dias de f2
                return True
        elif (f1[1] < f2[1]):   # si los meses no son iguales, con que el mes de f1 ...
            return True         # ... sea menor al mes de f2 retorno True
    elif (f1[0] < f2[0]):       # si los años no son iguales, con que el años de f1 ...
        return True             # ... sea menor al año de f2 retorno True
    return False                # si ningun condicion anterior se cumple f1 es fecha mayor


print(dias_entre((2019, 4, 28), (2019, 5, 12))) # 14 dias
print(dias_entre((2019, 4, 28), (2020, 5, 12))) # 380 dias
print(dias_entre((2019, 4, 28), (2022, 5, 12))) # 1.110 dias
print(dias_entre((2019, 4, 28), (2024, 5, 12))) # 1.841 dias
print(dias_entre((1997, 5, 12), (2020, 5, 12))) # 8.401 dias
print(dias_entre((2022, 5, 12), (2019, 4, 28))) # 1.110 dias
print(dias_entre((2022, 5, 12), (2019, 4, 48)))
print(dias_entre((2019, 4, 28), ("2019", 5, 12))) # 14 dias