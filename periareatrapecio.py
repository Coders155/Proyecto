basmay = float(input("Ingresa la longitud de la base mayor del trapecio: "))
basmen = float(input("Ingresa la longitud de la base menor del trapecio: "))
alt = float(input("Ingresa la altura del trapecio: "))
ladoizq = float(input("Ingresa la longitud del lado izquierdo del trapecio: "))
ladodere = float(input("Ingresa la longitud del lado derecho del trapecio: "))

area = ((bamay + basmen) * alt) / 2
perimetro = basmay + basmen + ladoizq + ladodere

print("El área del trapecio es:", area)
print("El perímetro del trapecio es:", perimetro)
