c0 = int(input("Digita un numero: "))

if c0 < 1:
    print('El numero es negativo o tiene 0.')
else:
    contador = 0

    while c0 != 1:
        if c0 % 2 == 0:
            c0 = int(c0 / 2)
        else:
            c0 = 3 * c0 + 1
        print(c0)
        contador += 1
    print("Total de numeros: ", contador)