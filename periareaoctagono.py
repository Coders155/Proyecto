lado = float(input("Ingresa la longitud del lado del octágono: "))

apotema = lado / (2 * math.tan(math.pi / 8))
perimetro = 8 * lado
area = (perimetro * apotema) / 2

print("El área del octágono es:", area)
print("El perímetro del octágono es:", perimetro)
