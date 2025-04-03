#Cálculo del tiempo total de un viaje con escalas
print("Hola, bienvenido a tu calculadora de horas de vuelos a escalas")
tramo1 = int(input("Ingrese el tiempo de vuelo del primer tramo: "))
escala1 = int(input("Ingrese el tiempo de la primera escala: "))

tramo2 = int(input("Ingrese el tiempo de vuelo del segundo tramo: "))
escala2 = int(input("Ingrese el tiempo de la segunda escala: "))

tramo3 = int(input("Ingrese el tiempo de vuelo del último tramo: "))

tiempo_total = (tramo1 + escala1) + (tramo2 + escala2) + tramo3
print("El tiempo total de viaje es de :", tiempo_total)
