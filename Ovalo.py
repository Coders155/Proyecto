import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

print ("OVALO")

r = int(input("Introduce el radio del Ovalo: "))

fig, ax = plt.subplots()

plt.title("OVALO")

ellipse = Ellipse((r, r/2), width=r*2, height=r, )
ax.add_patch(ellipse)
ax.set_xlim((0, r*2))
ax.set_ylim((0, r*2))
plt.show()
