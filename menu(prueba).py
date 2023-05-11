"""                LIBRERIAS                     """ 
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def limpiar_pantalla():
        
    os.system('cls' if os.name == 'nt' else 'clear')

"""-------------------------------------------------
-------------------------------------------------"""
"""                     MENU                     """
opccion=""

while (opccion != "s"):
    print("""
                    Menú
    -------------------------------------
    |¿Que figura necesitas?             |
    |-----------------------------------|
    | 1-Triangulo                       |
    | 2-Cuadrilatero                    |
    | 3-Pentagono                       |
    | 4-Hexagono                        |
    | 5-Circulos (Ovalos)               |
    | Presiona s + enter para salir     |                  
    -------------------------------------""")
    entrada=input("Ingresa la opción a elegir: ")
    if entrada == "s":
        break
    print("""-------------------------------------------------
    -------------------------------------------------"""
    """             MENU DE TRIANGULOS               """)
    if entrada==1:
        limpiar_pantalla()
        print(
            """   
                   Menú
        ---------------------------------
        | Tipos de triangulos           |
        ---------------------------------
        |1-Equilatero                   |
        |2-Escaleno                     |
        |3-Isosceles                    | 
        |4-opcion ant                   |
        |Presiona s + enter para salir  |
        ---------------------------------
        """
          )
        Ttriangulo=int(input("¿Cual tipo de triangulo necesitas? "))

    ################################################################
     ################## TRIANGULO EQUILATERO    ##################

    limpiar_pantalla ()
    if entrada == 1:
        if Ttriangulo == 1:
            print ("TRIANGULO EQUILATERO")
            a =int(input("Introduce el valor para todos los lados: "))
            fig, ax = plt.subplots()
            plt.title ("TRIANGULO EQUILATERO")
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
            print ("TRIANGULO EQUILATERO")
            ba = int (input("Inserte cm de Base: "))
            a = int (input("Inserte cm de Lado A: "))
            fig, ax = plt.subplots()
            plt.title ("TRIANGULO EQUILATERO")
            #El primero es para Este y Oeste
            #El segundo es para Norte y Sur
            ax.plot([0,ba], [0,0])##Base
            ax.plot([0,ba], [0,a])##Lado A
            ax.plot([ba, ba], [a,0])##Lado B
            ax.plot([ba,ba/2], [a,0])
            plt.show()

    ################################################################
     ################### TRIANGULO ISOSELES ######################

        elif Ttriangulo == 3:
            print ("TRIANGULO ISOSELES")
            a =int(input("Introduce el valor de la base (en cm): "))
            l = int(input("Introduce los valores de los lados (en cm): "))
            fig, ax = plt.subplots()
            plt.title ("TRIANGULO ISOSCELES")
            #El primero es para Este y Oeste
            #El segundo es para Norte y Sur
            ax.plot([0,a], [0,0]) ##Base
            ax.plot([0,(a/2)], [0,l]) ##Lado A
            ax.plot([(a/2),a], [l,0]) ##Lado B
            ax.plot([(a/2),(a/2)], [0,l]) ##Altura
            plt.show()

    """-------------------------------------------------
    -------------------------------------------------"""
    """       MENU DE FIGURAS DE UN SOLO LADO        """ 

    if entrada==5:
        limpiar_pantalla()
        print(
            """   
        ---------------------------------    
        |          Menú                 |
         --------------------------------
        |Tipos de Circulo u Ovalos      |
        ---------------------------------
        |1-Circulo                      |          
        |2-Ovoide                       |
        |3-Ovalo                        |
        |4.-opcion ant                  |
        |Presiona s + enter para salir  |
        --------------------------------- 
        """
          )
        TOval=int(input("¿Cual tipo de Circulo u Ovalo necesitas? "))

    ################################################################
     ##################        CIRCULO          ##################

    limpiar_pantalla()
    if TOval == 1:
        print ("CIRCULO")
        r = int (input("Introduzca el tamañano del radio que desea: "))
        fig, ax = plt.subplots()
        plt.title("CIRCULO")
        circle = plt.Circle((r, r), radius=r,)
        ax.add_patch(circle)
        ax.set_xlim((0, r*2))
        ax.set_ylim((0, r*2))
        plt.show()

    ################################################################
     ##################         OVALO           ##################

    elif TOval == 2:
        print ("OVALO")
        r = int(input("Introduce el radio del Ovalo: "))
        fig, ax = plt.subplots()
        plt.title("OVALO")
        ellipse = Ellipse((r, r/2), width=r*2, height=r, )
        ax.add_patch(ellipse)
        ax.set_xlim((0, r*2))
        ax.set_ylim((0, r*2))
        plt.show()

    ################################################################
     ##################        OVOIDE           ##################

    elif TOval == 3:
        print ("OVOIDE")
        r = int(input("Introduce el radio del Ovoide: "))
        fig, ax = plt.subplots()
        plt.title("OVOIDE")
        Ovoide = Ellipse((r, r), width=r, height=r*2, )
        ax.add_patch(Ovoide)
        ax.set_xlim((0, r*3))
        ax.set_ylim((0, r*3))
        plt.show()
    ################################################################
     ##################        Salida            ##################
