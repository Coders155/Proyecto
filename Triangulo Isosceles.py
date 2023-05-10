import matplotlib.pyplot as plt

print ("TRIANGULO ISOSELES")

a =int(input("Introduce el valor de la base (en cm): "))
l = int(input("Introduce los valores de los lados (en cm): "))
fig, ax = plt.subplots()

#El primero es para Este y Oeste
#El segundo es para Norte y Sur
ax.plot([0,a], [0,0]) ##Base
ax.plot([0,(a/2)], [0,l]) ##Lado A
ax.plot([(a/2),a], [l,0]) ##Lado B
ax.plot([(a/2),(a/2)], [0,l]) ##Altura
plt.show()