
import requerimiento_5

def R6(imprimir_3x4): #aÃ±o
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

    calendario = "Calendario del año " + str(imprimir_3x4) + " D.C \n"
    indice_primer_dia = requerimiento_5.R5(imprimir_3x4)
    primer_Dia_Mes = True
    contador_dias = indice_primer_dia
    
    for key, value in meses_dict.items():
        calendario += "\n" + "\t\t\t" + key + "\t\t" + "\nD\tL\tK\tM\tJ\tV\tS\n"
        dia = 1
        
        if (primer_Dia_Mes):
            calendario += contador_dias*"  \t"
            calendario += str(dia) + " \t"
            dia += 1
            contador_dias += 1
            primer_Dia_Mes = False
            
        while(dia <= value):
            contador_dias += 1
            if (contador_dias >= 7):
                contador_dias = 0
                calendario += "\n"
            calendario += str(dia) + " \t"
            dia += 1
            
        primer_Dia_Mes = True        
        
            
            
        
    print(calendario)
            
                    

















                
