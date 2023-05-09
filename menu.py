import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    

print("""
                Menú
-------------------------------------
|¿Que figura necesitas?             |
-------------------------------------
|1-Triangulo                        |
|2-Cuadrado                         |
|3-Rectangulo                       |
|4-Rombo                            |
|5-Romboide                         |
|6-Trapecio                         |
|7-Trapezoide                       |
|8-Poligono                         |
|9-Circulo                          |
|10-Ovalo                           |
-------------------------------------""")
figura=int(input("Ingrese la figura:"))
if figura==1:
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
    la1cua=int(input("Ingrese la medida de los lados:"))
    print("-------------------------------------- ")
elif figura==3:
    limpiar_pantalla()
    print("""Ingresa sus medidas
-------------------------------------- """)
    altrec=int(input("Ingrese la altura:"))
    anchrec=int(input("Ingrese el ancho:"))
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