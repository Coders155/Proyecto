import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    

print("""
                Menú
-------------------------------------
|¿Que figura necesitas?             |
-------------------------------------
|1-Triangulo                        |
|2-Cuadrilatero                     |
|3-Pentagono                        |
|4-Hexagono                         |
-------------------------------------""")
figura=int(input("Ingrese la figura:"))
if figura==1:
    #falta agregar los triangulos equilatero, cuadrilatero y isoseles
    limpiar_pantalla()
    print("""Ingresa sus medidas
-------------------------------------- """)
    caA=int(input("Ingrese medida cateto a:"))
    caB=int(input("Ingrese medida cateto b:"))
    hipo=int(input("Ingrese medida hipotenusa:"))
    print("-------------------------------------- ")
elif figura==2:
    limpiar_pantalla()
    print("""Ingresa sus medidas
-------------------------------------- """)
    la1cua=int(input("Ingrese la medida del lado1:"))
    la2cua=int(input("Ingrese la medida del lado2:"))
    la3cua=int(input("Ingrese la medida del lado3:"))
    la4cua=int(input("Ingrese la medida del lado4:"))
    print("-------------------------------------- ")
elif figura==3:
    limpiar_pantalla()
    print("""Ingresa sus medidas
-------------------------------------- """)
    la1pent=int(input("Ingrese la medida del lado1:"))
    la2pent=int(input("Ingrese la medida del lado2:"))
    la3pent=int(input("Ingrese la medida del lado3:"))
    la4pent=int(input("Ingrese la medida del lado4:"))
    la5pent=int(input("Ingrese la medida del lado5:"))
    print("-------------------------------------- ")
elif figura==4:
    limpiar_pantalla()
    print("""Ingresa sus medidas
-------------------------------------- """)
    la1rombo=int(input("Ingrese la medida del lado 1:"))
    la2rombo=int(input("Ingrese la medida del lado 2:"))
    la3rombo=int(input("Ingrese la medida del lado 3:"))
    la4rombo=int(input("Ingrese la medida del lado 4:"))
    print("-------------------------------------- ")    