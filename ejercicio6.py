#Cálculo del índice de masa corporal (IMC)
print("Hola, bienvenido a tu calculadora de IMC")
peso_kg = float(input("Ingrese el valor de su peso en kg: "))
altura_m = float(input("Ingrese su altura en metros: "))
imc = float(peso_kg / (altura_m * altura_m))
imc = imc * 100
imc = imc / 100
print("Su peso es de ", peso_kg)
print("Su altura es de ", altura_m)
print(f"Eso le da como resultado un IMC de {imc:.2f}")
print("IMC menor a 18.5: Peso insuficiente")
print("IMC entre 18.5 y 24.9: Peso normal o saludable")
print("IMC entre 25.0 y 29.9: Sobrepeso")
print("IMC de 30.0 o más: Obesidad")