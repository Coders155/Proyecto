def imprimir_tra(b):
    for i in range (b):
        for j in range (b-i):
            print(" ",end="")
        for i in range (i+b):
            print(" *",end="")
        print()


b = int(input("Escribe el numero de la base: "))
imprimir_tra(b)
