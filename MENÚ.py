"""                LIBRERIAS                     """ 
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse 
from matplotlib.patches import Polygon
import math
def limpiar_pantalla():
        
    os.system('cls' if os.name == 'nt' else 'clear')

"""-------------------------------------------------
-------------------------------------------------"""
"""                     MENU                     """
opccion=""

while (opccion != "s"):
    print("""        Menú
    -------------------------------------
    |¿Que figura necesitas?             |
    |-----------------------------------|
    | 1-Triangulo                       |
    | 2-Cuadrilatero                    |
    | 3-Pentagono                       |
    | 4-Hexagono                        |
    | 5-Circulos (Ovalos)               |
    | 10-salir                          |                  
    -------------------------------------""")
    entrada=int(input("Ingresa la opción a elegir: "))
    if entrada == 10:
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
        |4-opcion anterior              |
        |10-salir                       |
        ---------------------------------
        """)
        Ttriangulo=int(input("¿Cual tipo de triangulo necesitas? "))
        limpiar_pantalla ()
        if Ttriangulo == 10:
            break
        elif Ttriangulo == 1:
            
    ################################################################
     ################## TRIANGULO EQUILATERO    ##################
            m = int(input("Introduce la medida para todos los lados: "))
            fig, ax = plt.subplots()
            plt.title ("TRIANGULO EQUILATERO")
            lado = m
            altura = (math.sqrt(3)/2)*lado
            vertices = [(0, 0), (lado, 0), (lado/2, altura)]
            triangulo = Polygon(vertices, closed=True, facecolor='black')
            ax.add_patch(triangulo)
            ax.set_xlim((0, m*2))
            ax.set_ylim((0, m*2))
            plt.show()

    ################################################################
     #################### TRIANGULO ESCALENO ######################

        elif Ttriangulo == 2:
            print ("TRIANGULO EQUILATERO")
            b = int(input("Introduce la medida de la base: "))
            a = int(input("Introduce la medida de los lados: "))
            fig, ax = plt.subplots()
            plt.title ("TRIANGULO ESCALENO")
            vertices = [(0, 0), (b, 0), (b/2, a)]
            triangulo = Polygon(vertices, closed=True, facecolor='black')
            ax.add_patch(triangulo)
            ax.set_xlim((0, a*2))
            ax.set_ylim((0, a*2))
            plt.show()


    ################################################################
     ################### TRIANGULO ISOSELES ######################

        elif Ttriangulo == 3:
            print ("TRIANGULO ISOSELES")
            b = int(input("Introduce la medida de la base: "))
            a = int(input("Introduce la medida de los lados: "))
            fig, ax = plt.subplots()
            plt.title ("TRIANGULO ISOSCELES")
            vertices = [(0, 0), (b, 0), (b/2, a)]
            triangulo = Polygon(vertices, closed=True, facecolor='black')
            ax.add_patch(triangulo)
            ax.set_xlim((0, a*2))
            ax.set_ylim((0, a*2))
            plt.show()


    """-------------------------------------------------
    -------------------------------------------------"""
    """       MENU DE FIGURAS DE UN SOLO LADO        """ 

    if entrada==5:
        limpiar_pantalla()
        print("""   
        ---------------------------------    
        |          Menú                 |
         --------------------------------
        |Tipos de Circulo u Ovalos      |
        ---------------------------------
        |1-Circulo                      |          
        |2-Ovoide                       |
        |3-Ovalo                        |
        |4.-opcion ant                  |
        |10-salir                       |
        --------------------------------- 
        """)
        TOval=int(input("¿Cual tipo de Circulo u Ovalo necesitas? "))
        if TOval == 10:
            break

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
