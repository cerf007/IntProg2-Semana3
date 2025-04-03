# Conversión de una cantidad en dólares a distintas monedas 
print("Hola, bienvenido a tu calculadora de dolar en yenes, euros y libras")
dolares = float(input("Ingrese la cantidad de dólares a convertir: "))

#Estos valores fueron buscados en la web el 3 abril del 2025
yenes = dolares * 146.2
euros = dolares * 0.91
libras = dolares * 0.76

print("Tienes", dolares, "a cambiar")
print(f"De dólares a yenes serían: {yenes:.2f}")
print(f"De dólares a euros serían: {euros:.2f}")
print(f"De dólares a libras serían: {libras:.2f}")
