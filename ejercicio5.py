#Conversión de unidades de tiempo
print("Hola, bienvenido a tu calculadora de conversion de tiempo")
valor = int(input("Ingrese la cantidad de tiempo a convertir en segundos: "))
hora = int(valor / 3600)
seg_restantes = int(valor - (hora * 3600))
minutos = int(seg_restantes / 60)
seg_finales = int(seg_restantes - (minutos * 60))
print(valor," equivale a ", hora, " horas, ", minutos," minutos y ", seg_finales,"segundos" )