
semieje_mayor = float(input("Ingresa el semieje mayor del ovoide: "))
semieje_menor = float(input("Ingresa el semieje menor del ovoide: "))
semieje_vertical = float(input("Ingresa el semieje vertical del ovoide: "))

area = 2 * math.pi * semieje_menor**2 + (math.pi * semieje_menor * semieje_vertical)
volumen = (4/3) * math.pi * semieje_mayor * semieje_menor**2

print("El área del ovoide es:", area)
print("El volumen del ovoide es:", volumen)
