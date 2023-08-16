#Declaramos las variables y las inicializamos en 0
numero_par = 0
numero_impar = 0

#Pedimos al usuario que ingrese un numero
numero = int(input('Ingrese un numero: '))

#Iniciamos el bucle While

while numero != 0:
    if numero %2 == 1:
        #Incrementa el contador del numero impar (print(impar))
        numero_impar += 1
    else:
        #Incrementa los numeros pares
        numero_par += 1
        #volvemos a solicitar al usuario que ingrese un numero
    numero = int(input("Ingrese un numero: "))

#Imprimimos los resultados
print("Numeros pares: ",numero_par)
print("Numeros impares: ", numero_impar)
