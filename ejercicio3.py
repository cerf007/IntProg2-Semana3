#Cálculo del salario neto de un empleado
print("Bienvenido a tu calculadora de salario bruto")
salario_bruto = int(input("Ingrese el salario bruto del empleado: "))
imp_renta = float((salario_bruto) * 10/100)
seg_soc = float((salario_bruto) * 5/100)
pension = float((salario_bruto) * 3/100)
gastos = imp_renta + seg_soc + pension
salario_neto =  salario_bruto - gastos
print("El salario neto del empleado es de", salario_neto,)
print("De los cuales se descontaron ", imp_renta, "por impuestos sobre la renta,", seg_soc, "del seguro social", "y", pension, "de la pensión")