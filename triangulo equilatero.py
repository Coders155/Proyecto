import matplotlib.pyplot as plt
fig, ax = plt.subplots()
#El primero es para Este y Oeste
#El segundo es para Norte y Sur
n = int (input("Inserte cm de altura: "))
ax.plot([0,n], [0,0])##Base
ax.plot([0,(n/2)], [0,n])##Lado A
ax.plot([(n/2),n], [n,0])##Lado B
ax.plot([(n/2),(n/2)], [0,n])##Lado B
plt.show()