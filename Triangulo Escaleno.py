import matplotlib.pyplot as plt

print ("TRIANGULO EQUILATERO")

ba = int (input("Inserte cm de Base: "))
a = int (input("Inserte cm de Lado A: "))

fig, ax = plt.subplots()

plt.title ("TRIANGULO EQUILATERO")

#El primero es para Este y Oeste
#El segundo es para Norte y Sur
ax.plot([0,ba], [0,0])##Base
ax.plot([0,ba], [0,a])##Lado A
ax.plot([ba, ba], [a,0])##Lado B
ax.plot([ba,ba/2], [a,0])
plt.show()