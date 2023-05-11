import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

b = int(input("Itroduce la medida de la base: "))
a = int(input("Introduce la medida del cateto A: "))
fig, ax = plt.subplots()
vertices = [(0, 0), (1, a), (b, 1)]
triangulo = Polygon(vertices, closed=True, facecolor='red')
ax.add_patch(triangulo)
ax.set_xlim((0, b*2))
ax.set_ylim((0, a*2))
plt.show()

