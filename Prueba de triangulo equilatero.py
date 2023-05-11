import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math

m = int(input("Introduce la medida para todos los lados: "))

fig, ax = plt.subplots()
lado = m
altura = (math.sqrt(3)/2)*lado
vertices = [(0, 0), (lado, 0), (lado/2, altura)]
triangulo = Polygon(vertices, closed=True, facecolor='black')
ax.add_patch(triangulo)
ax.set_xlim((0, m*2))
ax.set_ylim((0, m*2))
plt.show()