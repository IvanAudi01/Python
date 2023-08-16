import random

num1 = random.randint(0,15)

if num1 == 0:
    print("Desayuna")
    print(" ")
elif num1 == 1:
    print("Tendras suerte el dia de hoy:)")
    print(" ")
elif num1 == 2:
    print("Echale ganas a la vida")
    print(" ")
elif num1 == 3:
    print("Suerte a la proxima")
    print(" ")
elif num1 == 4:
    print("Sera tu mejor dia")
    print(" ")
elif num1 == 5:
    print("Come sano")
    print(" ")
elif num1 == 6:
    print("El/ella no te ama")
    print(" ")
elif num1 == 7:
    print("Vuelve a intentar")
    print(" ")
elif num1 == 8:
    print("Dedicate a estudiar")
    print(" ")
elif num1 == 9:
    print("Eres alguien genial")
    print(" ")
elif num1 == 10:
    print("Eres lo mejor que puede pasarle a alguien")
    print(" ")
else:
    print("Vuelve a intentarlo es la opcion: ", num1)
    print(" ")



List = ["Desayuna","Tendras suerte el dia de hoy", "Echale ganas a la vida", "Suerte a la proxima", "Sera tu mejor dia", "Come sano", "El/ella no te ama", "Vuelve a intentar", "Dedicate a estudiar"]
List2 = ["Eres alguien genial", "Eres lo mejor que puede pasarle a alguien"]

Lista = List + List2
print(" ")

Lista5 = random.randint(0,15) 
print(" ")

if Lista5 <= 10:
    print(Lista[Lista5])
else:
    print("Vuelve a intentarlo, es la opcion:", Lista5)
