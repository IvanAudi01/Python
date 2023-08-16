Animal = []

print("-----------------------------------")
print("|                                 |")
print("|                                 |")
print("|  Veterinario mascota consentida |")
print("|                                 |")
print("|                                 |")
print("-----------------------------------")

while True:
    dato = input("¿Que opcion desea realizar: \n1.AGREGAR \n2.MOSTRAR \n3.ELIMINAR \n4.LIMPIAR \n6.ORDENAR \n5.SALIR \n-->")
    if dato == "AGREGAR":
        Animal = input("Agregar tipo de animal: \n")
        Animal = input("Raza de animal: \n")
        Animal = input("Motivo de consulta: \n")
        Animal = input("Tipo de alergias: \n")
        print(Animal)
    elif dato == "MOSTRAR":
        print(Animal)
    elif dato == "ELIMINAR":
        del Animal [-1]
    elif dato == "LIMPIAR":
        Animal.clear()
    elif dato == "ORDENAR":
        dato = input("Ordena ASCENDENTE o DESCENDENTE: ")
        if dato == "ASCENDENTE":
            Animal.sort()
        elif dato == "DESCENDENTE":
            Animal.reverse()
        else:
            print("Opcion incorrecta.")
        
       