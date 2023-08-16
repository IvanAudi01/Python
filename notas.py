#ESPATIFILIO
'''
entrada = input("Digite ESPATIFILIO o espatifilio: ")


if 'ESPATIFILIO' == entrada:
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
else:
    print("No, ¡quiero un gran Espatifilo")
'''

#///////////////////////////////////////////////////////////////////////////////////////////////
#CALCULADOR DE IMPUESTOS
'''
ingreso = float(input("Ingreso mensual: "))

if ingreso < 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = (ingreso - 85528) * .032 + 14839.02

if impuesto < 0.0:
    impuesto = 0.0

impuesto = round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
'''

#//////////////////////////////////////////////////////////////////////////////////////////////
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.
'''
odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)
'''
#/////////////////////////////////////////////////////////////////////////////////////////////
'''
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)
'''
#////////////////////////////////////////////////////////////////////////////////////////////
'''
numero_secreto = 777

numero = int(input('Ingrese un numero: '))

while numero != numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    int(input("¿Cual es el numero correcto: "))
print("¡Bien hecho, muggle! Eres libre ahora.")
'''

#///////////////////////////////////////////////////////////////////////////////////////////////
'''
import time             #Funcion para sleep

for tiempo in range(1, 10): #amos un rango a la durabilidad delo tiempo 
    print(tiempo,'Missisipi') #Imprimimos el tiempo y el mensaje
    time.sleep(tiempo)        #Hace el conteo del tiempo
print('Listos o no alla voy') #Mensaje al final del bucle
'''
#////////////////////////////////////////////////////////////////////////////////////////////

'''
#Ejemplo con break
print(("La instruccion break: "))
for i in range(1,6):
    if i == 3:   #Si el numero en el bucle iguala el 3 el programa termina de manera automatica
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

#Ejemplo continue
print("\nLa instruccion continue: ")
for i in range (1, 6):
    if i == 3:   #El programa detecta el 3 y no sale en el resultado y sigue rl proceso hasta el final.
        continue
    print("Dentro del bucle.", i)
print('Fuera del bucle.')
'''
#//////////////////////////////////////////////////////////////////////////////////////////////////
''' Break
largest_number = -99999999
counter = 0

while True: #No hay comparacion, se entra directamente en el bucle
    number = int(input("Ingresa un numero o escribe -1 para finalizar el programa: ")) #Pedimos al usuario que ingres eun numero
    if number == -1:   #Si el numero ingresa es igual a -1
        break  #Salimos del bucle
    counter += 1 #El contador aumenta
    if number > largest_number: #Si el numero ingresado es mayor al numero mas largo
        largest_number = number #Numero toma nuevo registro en la variable

if counter != 0:    #Si el contador es diferente de 0
    print("El numero mas grande es: ", largest_number)  #Seguira ciclando el mensaje 
else: 
    print("No has ingresado ningun numero: ") #En caso de no ingresar un numero de mostrara en pantalla

'''
'''
largest_number = -999999
counter = 0

number = int(input('Ingresa un numero o digita -1 para finalizar el programa: '))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number 
    number = int(input('Ingresa un numero o escribe -1 para finalizar el programa: '))

if counter:
    print("El numero mas grande es: ", largest_number)
else:
    print("No has ingresado ningun numero...")
'''
#/////////////////////////////////////////////////////////////////////////////////////////////
'''
while True:
    palabra = input("Escriba la palabra secreta: ")
    if palabra == 'chupacabra: ':
        print('Has dejado el bucle con exito:) ')
        break
'''
#///////////////////////////////////////////////////////////////////////////////////////////////
'''

palabra = input('Ingrese una palabra: ')
palabra = palabra.upper()

for letra in palabra:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        print(letra)
'''
#/////////////////////////////////////////////////////////////////////////////////////
'''
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
'''
#//////////////////////////////////////////////////////////////////////////////////
'''
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.

#El valor de la lista 4 pasa al valor 1 y se sustituye
numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.
'''
#////////////////////////////////////////////////////////////////////////////////////////
'''
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.
'''
#/////////////////////////////////////////////////////////////////////
'''
hat_list = [1, 2, 3, 4, 5]

numero = int(input("Ingrese un numero: "))
hat_list[2]= numero
print(hat_list)

del hat_list[4]
print("La longitud de la cadena es de: ", len(hat_list))
'''
#//////////////////////////////////////////////////////////////////////////////////////
#Happend
'''
my_list = []  # Creando una lista vacía.

for i in range(55):
    my_list.append(i + 1) #Se agrega un valor al final de la lista

print(my_list)
#////////////////////////////////////////////////////////////////////////////////////////
#insert
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

'''
#//////////////////////////////////////////////////////////////////////////////////////////
row = [WHITE_PAWN for i in range(8)]



