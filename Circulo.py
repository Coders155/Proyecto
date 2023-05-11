import matplotlib.pyplot as plt

print ("CIRCULO")

r = int (input("Introduzca el tamañano del radio que desea: "))

fig, ax = plt.subplots()

plt.title("CIRCULO")

circle = plt.Circle((r, r), radius=r,)
ax.add_patch(circle)
ax.set_xlim((0, r*2))
ax.set_ylim((0, r*2))
plt.show()