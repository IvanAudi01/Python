bloque = int(input("Ingrese el numero de bloques: "))
altura = 0
inlayer = 0

while inlayer <= bloque:
    altura += 1 
    bloque -= 1
    inlayer += 1

print("la altura de la piramide es: ", altura)
