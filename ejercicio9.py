#Cálculo del tiempo total de una película con comerciales
print("Bienvenido, somos tu calculadora de tiempo total de una película con comerciales")
dur_peli = float(input("Ingrese la duración de la película en minutos: "))
com_previos = float(input("Ingrese la duración de los comerciales previos: "))
pau_com = int(input("Ingrese la cantidad de pausas comerciales: "))
tiempo_comercial = float(input("Ingrese la duarción de cada pausa comercial:"))
tiempo_pausa = pau_com * tiempo_comercial
dur_peli_total = dur_peli + com_previos + tiempo_pausa
print("La pelicula originalmente dura", dur_peli, "minutos")
print("Los comerciales previos a la pelicula son de", com_previos, "minutos, y el total de tiempo de las pausas son de", tiempo_pausa, "minutos")
print("La duracion total de la pelicula es de:", dur_peli_total)