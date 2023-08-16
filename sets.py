#Los sets no llevan un orden.
nombres = {"Ivan", "Liliana", "Selene"}
nombres.add("Evelin")

edades = {21, 23, 43, 21}
edades.add(32)

#Aniadir un sett dentro de otro set
nombres.update(edades)

print(nombres, "\n")
print(len(nombres), "\n")
#remove se utiliza para eliminar elementos de las listas ////// si en la lista no existe un elemento discard lo evade y no lanza error
print(nombres, "\n")

nombres.remove("Ivan")
print(nombres)

nombres.pop()
print(nombres)
