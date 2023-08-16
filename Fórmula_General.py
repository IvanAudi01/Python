import math

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese un numero: "))
c = float(input("Ingrese un numero: "))

d = b ** 2-(4*a*c)

if d == 0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=x1
    print(f"El resultado es: {x1}, {x2}, son iguales...")
elif d>0:
     x1=(-b+math.sqrt(d))/(2*a)
     x2=(-b-math.sqrt(d))/(2*a)
     print(f"El resutado es: {x1}, {x2} ")
else:
     x=b/(2*a)
     im=math.sqrt(-d)
     print(f"El primer resultado complejo es: {x}+{im}i ")
     print(f"El primer resultado complejo es: {x}-{im}i ")

