class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.citas = []

    def agregar_cita(self, fecha, motivo):
        self.citas.append((fecha, motivo))

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Edad:", self.edad)
        print("Citas:")
        for fecha, motivo in self.citas:
            print("- Fecha:", fecha)
            print("  Motivo:", motivo)
        print()

def main():
    mascotas = []

    while True:
        print("Bienvenido al sistema de veterinario")
        print("1. Agregar mascota")
        print("2. Agregar cita")
        print("3. Mostrar información de mascota")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre de la mascota: ")
            especie = input("Ingrese la especie de la mascota: ")
            edad = input("Ingrese la edad de la mascota: ")
            mascota = Mascota(nombre, especie, edad)
            mascotas.append(mascota)
            print("Mascota agregada con éxito.\n")

        elif opcion == '2':
            nombre = input("Ingrese el nombre de la mascota: ")
            mascota_encontrada = None
            for mascota in mascotas:
                if mascota.nombre == nombre:
                    mascota_encontrada = mascota
                    break

            if mascota_encontrada:
                fecha = input("Ingrese la fecha de la cita: ")
                motivo = input("Ingrese el motivo de la cita: ")
                mascota_encontrada.agregar_cita(fecha, motivo)
                print("Cita agregada con éxito.\n")
            else:
                print("Mascota no encontrada.\n")

        elif opcion == '3':
            nombre = input("Ingrese el nombre de la mascota: ")
            mascota_encontrada = None
            for mascota in mascotas:
                if mascota.nombre == nombre:
                    mascota_encontrada = mascota
                    break

            if mascota_encontrada:
                mascota_encontrada.mostrar_info()
            else:
                print("Mascota no encontrada.\n")

        elif opcion == '4':
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()
