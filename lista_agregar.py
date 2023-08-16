nombre = ["Ivan", "Liliana", "Evelin"]
edad = [21, 21, 21]
calificacion = [True, False, True]

 #Anadir elementos a la lista en forma ordenada
nombre.append("Emiliano")
edad.append(20)
calificacion.append(False)

#Añadir elementos en la parte de a lista indicada
nombre.insert(3, "Paloma") 
edad.insert(3, "15")
calificacion.insert(3, True)

#Eliminar elementos de la lista
nombre.remove("Ivan")

#Limpiar toda la lista
nombre.clear()

print( nombre, "\n", edad, "\n", calificacion)

#Definir
persona = ["Carlos", "Maria", "Enrique"]

#Regresa un valor true o false dependiente de si el dato existe en la lista o no
print("Carlos" in persona)

#Nos regresa el valor en donde se encuentra
print(persona.index("Maria"))

#Se coloca el nombre en el lugar epicificado
persona [0] = "Jorge"
print(persona)

anios = [10, 21, 32]

anios [0] += 1

print(anios)
