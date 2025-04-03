#Cálculo del volumen de un cilindro y su área superficial
print("Bienvenido, soy tu calculadora de volumen y área superficial d cilindros")
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la alutra del cilindro: "))
area_base = float(3.1416 * radio * radio)
volumen_cilindro = float(area_base * altura)
#Para el área superficial se necesita el área lateral
area_lateral = float(2 * 3.1416 * radio * altura)
area_superficial = float((area_lateral) + 2 * (area_base))
print("El radio del cilindro es: ", radio, "y su altura es: ", altura)
print("El volumen del cilindro es de: ", volumen_cilindro)
print("El área superficial del cilindro es de: ", area_superficial)
