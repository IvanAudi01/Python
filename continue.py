#Inicializamos las variables en 0
numero = 0
contador = 0

#Peidmos alusuario que ingrese un numero
numero1 = int(input('Ingresa un numero o teclea -1 para finalizar el programa: '))

#Iniciamos el ciclo while, mientras numero1 sea diferente de -1
while numero1 != -1:
    if numero == -1: #Si numero es igual a -1 termina el programa
        continue
    contador += 1       #Contador aumenta 1

    if numero1 > numero:    #Si numero1 es mayor a numero 
        numero =  numero1   #Numero1 sustituye el valor de numero
    #Volvemos a ingresar un numero
    numero = int(input('Ingresa un numero o teclea -1 para finalizar el programa: '))

#Si contador termina lanza el resultado del numero mas grande
if contador:
    print('El numero, mas grande es: ', numero)
else:
    print('No has ingresado ningun numero.')