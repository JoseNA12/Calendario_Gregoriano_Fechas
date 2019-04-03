# R1(bisiesto): Dado un año perteneciente al rango permitido, determinar si este es bisiesto.
# El resultado debe ser un valor booleano, True o False

def R1(bisiesto):
	if (type(bisiesto) is int):																														# Comprobar que el año ingresado sea número entero
		if (((bisiesto % 4) == 0) and ((bisiesto % 100) != 0)) or ((bisiesto % 400) == 0):	# Un año es bisiesto si:
			return True																																				# .. es divisible entre 4 y no entre 100 
		else:																																								# .. o si es divisible entre 400
			return False
	else:
		return False
