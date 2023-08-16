numero_secreto = 777

print("""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input('Ingrese un numero: '))

while numero != 0:
    if numero != numero_secreto:
        print("!ja, ja, Estas atrapado en mi bucle!")
    else:
        print('Felicidades acertaste, tuvite suerte, nos vemos a la proxima...')
        numero = int(input("Ingrese un numero nuevamente: "))

    
    