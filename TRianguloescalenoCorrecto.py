lado = int(input("Ingrese la medida del lado de la figura un entero positivo: "))
print("triamgulo Escaleno:")

def imprimir_trianguloEsc(lado):
   for i in range(lado):
       for j in range(lado-i):
           print("", end=" ")
       for j in range(2*i+1):
           print("*", end=" ")
       print()

imprimir_trianguloEsc(lado)
