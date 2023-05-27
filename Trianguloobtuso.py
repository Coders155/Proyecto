def imprimir_tri(ba):
    for i in range (ba+1):
        for j in range(i+ba):
            print (" ", end=" ")
        for i in range (i):
            print (" ", end="*")     
        print()  
ba=int(input("Escribe la medida de la base "))

imprimir_tri(ba)
