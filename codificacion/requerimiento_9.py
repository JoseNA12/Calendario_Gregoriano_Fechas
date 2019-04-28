#dia_semana(fecha): Dada un fecha determinar el día de la semana que le corresponde.
#El resultado debe ser un número entero según corresponde en la siguiente codificación:
#   0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado.
"""
Entradas: "fecha": Es una fecha con el formato (año,mes,día).
Salidas: El número del día correspondiente a la fecha según los siguientes valores:
         0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado.
Restricciones: El año ingresado debe de ser mayor a 1582, que es cuando se empieza a utilizar el calendario Gregoriano.
"""
import requerimiento_2
import requerimiento_5

def dia_semana (fecha):
    if(fecha[0]>1582):      #Se verifica que el año pertenezca al calendario Gregoriano(año>1582)
        if(requerimiento_2.R2(fecha)):              #Se verifica que sea un fecha válida
            return requerimiento_5.calcularDoomsday(fecha)  #Se calcula el día de la semana que es la fecha ingresada
        else:
            return "La fecha ingresada no es válida"
    else:
        return "El año no pertenece al claendario Gregoriano. Debe ser mayor a 1582"
        
    
    
