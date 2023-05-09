import matplotlib.pyplot as plt
fig, ax = plt.subplots()
#El primero es para Este y Oeste
#El segundo es para Norte y Sur
n = input ("Inserte cm de base: ")
ax.plot([0,n], [1,1])##Linea azul
ax.plot([0,1.5], [1,3])##Linea verde
ax.plot([1.5,3], [3,1])##Linea naranja
plt.show()
