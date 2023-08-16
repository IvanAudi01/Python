class Nodo:             #Nombre     #Cedula     #Apuntador a siguiente dato
    def __init__(self, nombre=None, cedula=None, sig=None):
        self.nombre = nombre #atributos de la clase
        self.cedula = cedula #atributos de la clase
        self.sig = sig       #atributos de la clase
    #Cambiar el dato que ya hemos escrito
    def __str__(self):
        return "%s %s" %(self.nombre, self.cedula) #Concatenacion de nombre y cedula

class lSimples:
    #Constructor {Inicializa los atributos por defecto de la clase}
    def __init__(self):
     self.cabeza = None #Guardar lista
     self.cola = None   #Tener la ultima referencia del ultimo nodo
    
    #Se crea la funcion de agregar
     def agregar(self, elemento):
        if self.cabeza == None:
           self.cabeza = elemento

        if self.cola != None:
            self.cola.sig = elemento

        self.cola = elemento       

#Probrar si agregar funciona 
if __name__ == "__main__":
    ls = lSimples() #Intanciamos el objeto.

    #Creamos el menu con ciclo While
    while(True):
       print("----Menu----\n"+
             "1. Agregar")
       num = input("Ingrese un numero: ")
       if num == "1":
          nombre =input('Ingrese el nombre: ')
          cedula = input('Ingrese la cedula: ')
          nod = Nodo(nombre, cedula)
          ls.agregar(nod)
