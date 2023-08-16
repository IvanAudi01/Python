#Las tuplas no pueden ser modificadas en el proceso

alumnos = ("Ivan", "Liliana", "Selene")
edades = (21, 21, 35)
calificacion = (True, True, False)

edadIvan =  edades[0]
edadIvan += 1

print(edadIvan)