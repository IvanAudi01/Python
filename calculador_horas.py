hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
duracion = int(input("ingrese la duracion: "))

minutos = minutos + duracion
hora = hora + minutos // 60
minutos = minutos % 60
hora = hora % 24
print(hora, ':', minutos, sep=" ")
