#Pedir al usuario 3 numeros
num1 = int(input("Ingrese el primero numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero:  "))

#Numero 1 cae en la variable
numprueba = num1
 #Comparamos la variable con el segundo numero
if numprueba < num2:
    numprueba = num2

#Comparamos el tercer numero
if numprueba < num3:
    numprueba = num3

print(numprueba)

'''
# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.

#Para encontrar el minimo se puede usar min()
largest_number = max(number1, number2, number3)

# Imprime el resultado.
print("El número más grande es:", largest_number)


'''