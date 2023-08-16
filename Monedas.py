#LIBRERIA PARA NUMEROS RANDOM
import random

num1 = random.randint(0,10)

rango = int(input("Ingrese un numero: "))

if rango < num1:
    print("Es cara")
else:
    print("Es sello")
