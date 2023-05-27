def imprimir_triangulorectangulo(lado):

   for i in range(lado):

       for j in range(lado-i):

           print("", end="")

       for j in range(2*i+1):

           print("*", end=" ")

       print()

lado = int(input("Ingrese la medida del lado de la figura un entero positivo: "))

print("triamgulo rectangulo:")

imprimir_triangulorectangulo(lado)
