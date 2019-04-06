# R6 (imprimir_3x4): Dado un año perteneciente al rango permitido, desplegar en consola el
# calendario de ese año en formato de 3 secuencias (‘filas’) de 4 meses cada una. El resultado debe
# lucir semejante al que se muestra al final de este enunciado.



import requerimiento_1
import requerimiento_5

"""
Entradas: Recibe un entero que representa el año del calendario que desea mostrar
Salidas: Muestra un string que representa el calendario del año indicado
Restricciones: El número ingresado debe ser entero y válido para el calendario gregoriano
"""

def R6(imprimir_3x4): 
    meses_dict = {	    # Diccionario con los meses y la cantidad dias respectivamente
        "Enero": 31,
        "Febrero": 28,
        "Marzo": 31,
        "Abril": 30,
        "Mayo": 31,
        "Junio": 30,
        "Julio": 31,
        "Agosto": 31,
        "Septiembre": 30,
        "Octubre": 31,
        "Noviembre": 30,
        "Diciembre": 31
    }

    dias = ("D", "L", "K", "M", "J", "V", "S")
    print("Calendario del año " + str(imprimir_3x4) + " D.C")
    lista_meses = []
    item_mes = []   
    dia_inicial = requerimiento_5.R5(imprimir_3x4) # Obtener el dia en el que empieza el dia de enero   
    if (type(dia_inicial) is not int):  # Validar el tipo de dato del año ingresado
        return "Año inválido"
    if (requerimiento_1.R1(imprimir_3x4)):  # Verificar si el año ingresado es bisiesto. Si es, se añade +1 dia al mes de febrero
        meses_dict["Febrero"] = meses_dict.get("Febrero") + 1
    for _mes, cant_dias in meses_dict.items():  # Iterar sobre el diccionario de meses y sus cantidades de dias respectivos
        lista_temp=[]
        for _dia in dias:   # Ingresar los dias de la semana en cada mes
            lista_temp.append(_dia);
        item_mes.append(lista_temp)
        temp_ceros = dia_inicial
        lista_temp = []
        while temp_ceros != 0: # Anadir espacios vacios acorde al dia inicial del mes
            lista_temp.append(" ")
            temp_ceros -= 1
        for _dia in range(1, cant_dias + 1):    # Recorrer los dias segun la cantidad respectiva
            lista_temp.append(_dia)
            dia_inicial += 1
            if (dia_inicial == 7): # Si es el dia final de la semana, insertar lista con la cantidad de 7 dias, luego se inicia en []
                item_mes.append(lista_temp)
                lista_temp = []
                dia_inicial = 0
        temp_ceros = dia_inicial
        while temp_ceros != 7: # Ingresar ceros en la matriz acorde al dia de inicio
            lista_temp.append(" ")
            temp_ceros += 1        
        item_mes.append(lista_temp)
        if(len(item_mes)!=7): # Para que todos los meses sean de tamaño 7. 
            item_mes.append([" "," "," "," "," "," "," "])
        lista_meses.append(item_mes)
        item_mes = []
    imprimir_R6(lista_meses,imprimir_3x4)


"""
Entradas: Recibe una matriz que representa el calendario y un entero que es el año del calendario
Salidas: Muestra un string que representa el calendario del año indicado
Restricciones: El número ingresado debe ser entero y válido para el calendario gregoriano
"""

def imprimir_R6(calendario,anio):
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    cantidad = 4
    strs = "Calendario del año "+ str(anio) + "DC\n"
    num_mes = 0
    for c in range(0,len(calendario),4):# Repite el proceso hasta completar todos los meses del año. Va de 4 en 4
        filas = len(calendario[c])
        print(meses[c] + " "*(30-len(meses[c])),end="") #Se agregan los nombres de los meses correspondientes. Se resta 30 caracteres que cubre cada mes menos la cantidad del nombre 
        print(meses[c+1] + " "*(30-len(meses[c])),end="")
        print(meses[c+2] + " "*(30-len(meses[c])),end="")
        print(meses[c+3] + " "*(30-len(meses[c])),end="\n")  
        for j in range(filas): # Recorre todas las filas de la matriz
                strsFila = ""
                for i in range(num_mes,cantidad): # Establece la cantidad de meses a mostrar por fila
                    for k in range(len(calendario[i][j])): #Recorre cada  elemento. La idea es ir aumentando k, luego i y por último j.
            
                        if (type(calendario[i][j][k]) is int) and (calendario[i][j][k]>9): # Si es un número mayor a 9 disminuir los espacios añadidos para que no se descuadre
                            strsFila += str(calendario[i][j][k])+" "
                        else:
                            strsFila += str(calendario[i][j][k])+"  " # Si es núm de un dígito añadir un espacio más
                        if((k % 6 == 0) and (k!=0)):
                            strsFila += " |   "
                print(strsFila)
        num_mes += 4 # Cuando se terminan los primeros 4 meses se continúan con los siguientes 4
        cantidad += 4 # Se establece un nuevo tope de meses
        print("=====================================================================================================")














                
