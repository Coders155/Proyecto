"""                LIBRERIAS                     """ 
import os
import matplotlib.pyplot as plt

"""-------------------------------------------------
-------------------------------------------------"""
"""                     MENU                     """

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
print("""
                Menú
-------------------------------------
|¿Que figura necesitas?             |
-------------------------------------
| 1-Triangulo                       |
| 2-Cuadrilatero                    |
| 3-Pentagono                       |
| 4-Hexagono                        |
-------------------------------------""")
entrada=int(input("Ingrese la figura: "))

"""-------------------------------------------------
-------------------------------------------------"""
"""             MENU DE TRIANGULOS               """ 

if entrada==1:
    limpiar_pantalla()
    print(
        """   
               Menú
    -------------------------
    |  Tipos de triangulos  |
    -------------------------
    |       1-Equilatero    |
    |       2-Escaleno      |
    |       3-Isoceles      |
    -------------------------
    """
      )
    Ttriangulo=int(input("¿Cual tipo de triangulo necesitas? "))

################################################################
 ################## TRIANGULO EQUILATERO    ##################

limpiar_pantalla ()
if entrada == 1:
    if Ttriangulo == 1:
        print ("TRIANGULO EQUILATERO")
        a =int(input("Introduce el valor de la altura (en cm): "))
        fig, ax = plt.subplots()
        #El primero es para Este y Oeste
        #El segundo es para Norte y Sur
        ax.plot([0,a], [0,0]) ##Base
        ax.plot([0,(a/2)], [0,a]) ##Lado A
        ax.plot([(a/2),a], [a,0]) ##Lado B
        ax.plot([(a/2),(a/2)], [0,a]) ##Altura
        plt.show()
        
################################################################
 #################### TRIANGULO ESCALENO ######################

    elif Ttriangulo == 2:
        print ("TRIANGULO ESCALENO")
        fig, ax = plt.subplots()
        ba = int(input("Introduce el valor de la Base (en cm): "))
        a = int(input("Introduce el valor del Lado A (en cm): "))
        #El primero es para Este y Oeste
        #El segundo es para Norte y Sur
        ax.plot([0,ba], [0,0])##Base
        ax.plot([0,ba], [0,a])##Lado A
        ax.plot([ba, ba], [a,0])##Lado B
        plt.show()

################################################################
 ################### TRIANGULO ISOSELES ######################

    elif Ttriangulo == 3:
        print ("TRIANGULO ISOSELES")
        a =int(input("Introduce el valor de la base (en cm): "))
        l = int(input("Introduce los valores de los lados (en cm): "))
        fig, ax = plt.subplots()
        #El primero es para Este y Oeste
        #El segundo es para Norte y Sur
        ax.plot([0,a], [0,0]) ##Base
        ax.plot([0,(a/2)], [0,l]) ##Lado A
        ax.plot([(a/2),a], [l,0]) ##Lado B
        ax.plot([(a/2),(a/2)], [0,l]) ##Altura
        plt.show()