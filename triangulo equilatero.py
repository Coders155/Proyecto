import matplotlib.pyplot as plt
fig, ax = plt.subplots()
#El primero es para Este y Oeste
#El segundo es para Norte y Sur
a = int (input("Inserte cm de altura: "))
ax.plot([0,a], [0,0])##Base
ax.plot([0,(a/2)], [0,a])##Lado A
ax.plot([(a/2),a], [a,0])##Lado B
ax.plot([(a/2),(a/2)], [0,a])##Altura
plt.show()