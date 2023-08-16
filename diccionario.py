#Primero va la clave y despues el objeto que se va a poder modificar y se separa por : y al pasar al siguiente dato se separa
#por una coma

alumno = {"Ivan": 21, "Sergio": 32, "Amanda": 15}
#Modificar valores de un diccionario
alumno["Ivan"] = 22
#Agregamos un nuevo usuario al diccionario
alumno["Omar"] = 45
print(alumno, '\n')


'''
print(alumno["Ivan"]) #Se busca por la clave del objeto
print(alumno.get("Sofia", "No esta en el diccionario")) #Con GET se puede consultar tambien y permite agregar un argumento en caso de que no este la clave 
'''