'''for numero in range(101):
    if numero %3 == 0 and numero %5 == 0:
        print("FizzBuzz")
    elif numero %3 == 0:
        print("Fizz")
    elif numero %5 == 0:
        print('Buzz')
    else:
        print(numero)
'''
while True:
    numero = int(input("Ingrese un numero: "))
    if numero %3 == 0 and numero %5 == 0:
        print("FIZZ BUZZ")
    elif numero %3 == 0:
        print("FIZZ")
    elif numero %5 == 0:
        print("BUZZ")
    else:
        print("Intenta otra vez...")
    print(numero)