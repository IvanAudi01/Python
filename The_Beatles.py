#Paso 1
beatles = []

#Paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

#Paso 3
for miembros in range(2): #Permite agfregar 2 elementos a la lista
    beatles.append(input("Ingrese un miembro a la banda: "))
print(beatles)

#Paso 4
del beatles[-1]
del beatles[-1]

#Paso 5 
beatles.insert(0, "Ringo Starr")
print(beatles)