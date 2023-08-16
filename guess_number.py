num = 0
adivina = 0

while num != 6 and adivina < 5:
    num = int(input("Ingresa un numero: "))

if adivina != 6:
    print("Felicidades acertaste:)")
else:
    print("Se terminaron tus intentos")