nombre = ["Ivan", "Liliana", "Evelin"]
edad = [21, 21, 21]
calificacion = [True, False, True]
colores = ["rojo", "azul", "verde", "negro", "amarillo"]


#Cuenta la cantidad de datos que se repiten dentro de la lista
print(edad.count(21))

#Incluye los elemntos de una lista dentro de otra lista
edad.extend(nombre)
print(edad)

#Elimina un elemento de la lista y lo devuelve
print(colores.pop(2)) #Si agregarmos un numero dentro del parentesis se elimina el elemento
print(colores)        #que este en la tabla

#Cambia el orden de la lista
colores.reverse()
print(colores)
