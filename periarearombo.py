diamay = float(input("Ingresa la longitud de la diagonal mayor del rombo: "))
diamen = float(input("Ingresa la longitud de la diagonal menor del rombo: "))

area = (diamay * dianmen) / 2
perimetro = 4 * ((diamay ** 2 + diamen ** 2) ** 0.5) / 2

print("El área del rombo es:", area)
print("El perímetro del rombo es:", perimetro)
