import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

print ("OVOIDE")

r = int(input("Introduce el radio del Ovoide: "))

fig, ax = plt.subplots()

plt.title("OVOIDE")

Ovoide = Ellipse((r, r), width=r, height=r*2, )
ax.add_patch(Ovoide)
ax.set_xlim((0, r*3))
ax.set_ylim((0, r*3))
plt.show()
