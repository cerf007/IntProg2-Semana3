# Cálculo del precio final de un producto con impuestos y descuentos
print("Bienvenido a tu calculadora de descuentos")
precio = float(input("Ingrese el precio original del producto: "))
porcentaje = int(input("Ingrese el la cantidad de descuento a aplicar: "))
descuento =  float(precio * (porcentaje/100))
precio_descontado = precio - descuento
porcent_iva = float(input("Ingrese el  porcentaje del IVA: "))
iva =  float(precio_descontado * (porcent_iva/100))
precio_final = float(precio_descontado + iva)
print("El valor incial del producto es de ", precio)
print("Se le aplico un descuento del", porcentaje, "%",)
print("El precio con el descuento aplicado es de: ", precio_descontado)
print("Ahora con un IVA de", porcent_iva, "%", "se añaden", iva, "por impuestos")
print("Asi el precio final nos da: ", precio_final)
