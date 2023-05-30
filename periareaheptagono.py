lado = float(input("Ingresa la longitud del lado del heptágono: "))

apotema = lado / (2 * (0.tan(math.pi/7)))
perimetro = 7 * lado
area = (perimetro * apotema) / 2

print("El área del heptágono es:", area)
print("El perímetro del heptágono es:", perimetro)
