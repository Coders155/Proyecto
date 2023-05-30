#necesitamos base, altura (Qque vienen siendo los catetos) y la hipotenusa
#co= altura, ca= base, h= hipotenusa
import math
co= int(input())#Estas se borran y se sutituyen por los valores que tengamos
ca= int(input())
h= int(input())
sen=co/h
print("Seno=", sen )
angs = math.asin(sen)
print(F"El ∡ resultante usando senoA es de = {math.degrees(angs)}")
cos=co/h
print("Coseno=", cos)
angc = math.acos(cos)
print(f"El ∡ resultante usando coseno es de = {math.degrees(angc)}")
tan=co/h
med= math.degrees(angc)+math.degrees(angs)
print ("Tangente=", tan) 
angt= math.atan(tan) 
print(f"El ∡ resultante es de = {180-med}")
cosec=h/co
print("Cosecante=", cosec)
sec=h/ca
print("Secante=", sec)
conta=ca/co
print("Contangente es=", conta)
