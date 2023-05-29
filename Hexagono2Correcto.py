lado = int(input("Lado: "))
espacios = lado-1
for i in range(lado, 3*lado, 2):
	print ("  "*espacios + " *"*i)
	espacios -= 1
espacios = 1
for i in range(3*lado-4, lado-2, -2):
	print ("  "*espacios + " *"*i)
	espacios += 1
