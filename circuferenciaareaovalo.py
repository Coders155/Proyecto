semieje_mayor = float(input("Ingresa el semieje mayor de la elipse: "))
semieje_menor = float(input("Ingresa el semieje menor de la elipse: "))

area = math.pi * semieje_mayor * semieje_menor
circunferencia = 2 * math.pi * math.sqrt((semieje_mayor ** 2 + semieje_menor ** 2) / 2)

print("El área de la elipse es:", area)
print("La circunferencia de la elipse es:", circunferencia)
