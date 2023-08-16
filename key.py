import keyboard
import time

segundos = int(input("Cuantos segundos desea bloquear el teclado: "))

for i in range(150):
    keyboard.block_key(i)

time.sleep(segundos)