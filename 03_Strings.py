###Strings###
print(" ")
print('\t\t\t"""String"""')
print(" ")

firstChar = 'Ivan'
secondChar = 'Audiffred'

print(len(firstChar))
print(len(secondChar))

print(firstChar + ' ' + secondChar)

#Salto de linea
tirdthChar = 'Hoy es mi dia \n manana tambien'
print(tirdthChar)

#Tabulacion
tirdthChar = '\t\t\tHoy es mi dia manana tambien'
print(tirdthChar)
print("")

name, age, city = "Ivan", 21, "Mexico"

print("My name is: ", name, "and i'm: ", age, "year old", "and i live on ", city)
print(' ')

#.format es con {}
print("Mi nombre es {} y mi edad es {}, mi nacionalidad es {}".format(name, age, city))
#%s es con %     #%d para numeros
print("Mi nombre es %s y mi edad es %d, mi nacionalidad es %s"%(name, age, city))

#Inferencia de datos
print(f"Mi nombre es {name} y mi edad es {age}, mi nacionalidad es {city}")
print(' ')

#Desempaquetado de caracteres
lenguaje = 'python'
a, b, c, d, e, f = lenguaje
print(a)
print(b)

#Division

lenguajepy = lenguaje[1:6]
print(lenguajepy)

lenguajepy = lenguaje[::-1]
print(lenguajepy)

lenguajepy = lenguaje[0:6:2]
print(lenguajepy)

#Metodos o funciones

print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.lower())
print(lenguaje.count('o'))
print(lenguaje.isnumeric())
print('1'.isnumeric())
print(lenguaje.upper().isupper())
print(lenguaje.startswith('oy'))
print(' ')