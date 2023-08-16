
estatura = float(input("Ingrese la estatura a la persona: "))
credito = int(input("Ingrese numero de creditos: "))
print(" ")

if estatura < 1.40:
    print("No tiene la altura necesaria para poder subir al juego.","\n", "La altura es de: ",estatura)
else:
    print("Puedes pasar, diviertete:) ")
print(" ")
if credito < 50:
    print("Los creditos son insuficientes.","\n","La cantidad de creditos son: ",credito)
else:
    print("Puedes pasar, diviertete:)")
print(" ")

if estatura > 1.49 and credito > 49:
    print("Puedes pasar diviertete.")
elif estatura > 2.49 or credito >49:
    print("Una condicion no se cumple, no vemos...")
else:
    print("No cumples con las condiciones, lo siento:(")
print(" ")

