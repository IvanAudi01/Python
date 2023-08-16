torneo = []

while True:
    equipo = input("Ingrese una opcion: \n1.AGREGAR \n2.MOSTRAR \n3.ELIMINAR \n4.LIMPIAR \n6.ORDENAR \n5.SALIR \n-->")
    #AGREGAMOS ELEMENTOS A LA LISTA
    if equipo == "AGREGAR":
        torneo.append(input("\nIngrese un equipo a la lista: \n"))
    #MOSTRAMOS LOS ELEMENTOS DE LA LISTA    
    elif equipo == "MOSTRAR":
        print(" ")
        print(torneo, "\n")
    #ELIMINAMOS ELEMENTOS DE LA LISTA
    elif equipo == "ELIMINAR":
        del torneo[-1]
        print(" ")
    #LIMPIAMOS LOS DATOS DE LA LISTA
    elif equipo == "LIMPIAR":
        torneo.clear()
        print(" ")
    elif equipo == "ORDENAR":
        equipo = input("Elige un orden para ordenar: ")
        if equipo == "ASCENDENTE":
            torneo.sort()
        elif equipo == "DESCENDENTE":
            torneo.reverse()
        else:
            print("Opcion invalida, intenta otra vez...")
        print(torneo)
    #SALIMOS DE LA LISTA
    elif equipo == "SALIR":
        break
    else:
        print("Esa opcion es incorrecta, intenta otra vez...")
print(torneo)