yuan = 0.14   #DLS
yen = 0.0073  #DLS
won = 0.00076 #DLS

#PEDIMOS AL USUARIO INGRESAR LA CANTIDAD DE DINERO
dolar = int(input("Ingrese la cantida de dolares: "))
#yuan = float(input("Ingrese la cantidad de 'YUAN' a convertir: "))
#yen = float(input("ingrese la cantidad de 'YEN' a convertir: "))
#won = float(input("Ingrese la cnatdad de 'WON' a convertir: "))

#HACEMOS LA OPERATICION DE CALCULO
total = yuan * dolar
total1 = yen * dolar
total2 = won * dolar

print(" ")
#MOSTRAMOS EL RESULTADO
print("La cantidad en 'YUAN' es: ", total, "yuans" "\n")
print("La catidad en 'YEN' es: ", total1, "yens" "\n")
print("La cantidad en 'WON' es: ", total2, "wons" "\n") 

#SE CONCATENAN LAS 3 CONVERSIONES
print(total + total1 + total2)