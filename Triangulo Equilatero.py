import matplotlib.pyplot as plt

print ("TRIANGULO EQUILATERO")

a =int(input("Introduce el valor para todos los lados: "))


fig, ax = plt.subplots()

plt.title ("TRIANGULO EQUILATERO")

#El primero es para Este y Oeste
#El segundo es para Norte y Sur
ax.plot([0,a], [0,0]) ##Base
ax.plot([0,(a/2)], [0,a]) ##Lado A
ax.plot([(a/2),a], [a,0]) ##Lado B
ax.plot([(a/2),(a/2)], [0,a]) ##Altura
plt.show()