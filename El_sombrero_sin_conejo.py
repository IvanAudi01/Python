hat_list = [1, 2, 3, 4, 5]

numero = int(input("Ingrese un numero: ")) #Pedimos al usuario que ingrese un numero
hat_list[2] = numero #Reemplazamos el numero ingresado por el de la posicion 2 en la lista

#Imprimimos la lista
print(hat_list)

#Eliminamos el numero en la lista
del hat_list[4]
print(hat_list)

#Imprimimos la cantidad de la lista  
print("La extension de la lista es de: ", len(hat_list))