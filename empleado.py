
class Empleado:
    def __init__(self, nombre, id_empleado, puesto, salario):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.puesto = puesto
        self.salario = float(salario)

    def informacion(self):
        print(f"Nombre: {self.nombre}, ID: {self.id_empleado}, Puesto: {self.puesto}, Salario: ${self.salario:.2f}")


lista_empleados = []

while True:
    print("--- Menú Empleados ---")
    print("1. Agregar Empleado")
    print("2. Mostrar información de un empleado")
    print("3. Modificar empleado")
    print("4. Mostrar todos los empleados")
    print("5. Eliminar empleado")
    print("6. Salir")

    try:
        opcion = int(input("¿Qué opción desea realizar?: "))
    except ValueError:
        print("Opción inválida, escribe un número del 1 al 6.")
        continue

    if opcion == 1:
        nombre = input("Nombre del empleado: ")
        id_empleado = input("ID del empleado: ")
        puesto = input("Puesto: ")
        salario = input("Salario: ")

        nuevo_empleado = Empleado(nombre, id_empleado, puesto, salario)
        lista_empleados.append(nuevo_empleado)
        print("Empleado agregado.")

    elif opcion == 2:
        id_empleado = input("Ingrese el ID del empleado: ")
        encontrado = False
        for empleado in lista_empleados:
            if empleado.id_empleado == id_empleado:
                empleado.informacion()
                encontrado = True
                
        if not encontrado:
            print("Empleado no encontrado.")

    elif opcion == 3:
        id_empleado = input("Ingrese el ID del empleado a modificar: ")
        for empleado in lista_empleados:
            if empleado.id_empleado == id_empleado:
                print("Datos actuales:")
                empleado.informacion()

                empleado.nombre = input("Nuevo nombre (Enter para no cambiar): ") or empleado.nombre
                empleado.puesto = input("Nuevo puesto (Enter para no cambiar): ") or empleado.puesto
                nuevo_salario = input("Nuevo salario (Enter para no cambiar): ")
                if nuevo_salario:
                    empleado.salario = float(nuevo_salario)

                print("Datos actualizados.")
                
        else:
            print("Empleado no encontrado.")

    elif opcion == 4:
        if not lista_empleados:
            print("No hay empleados registrados.")
        else:
            print("Lista de Empleados:")
            print(f'{"ID":<10} {"Nombre":<15} {"Puesto":<15} {"Salario":<10}')
            for empleado in lista_empleados:
                print(f'{empleado.id_empleado:<10} {empleado.nombre:<15} {empleado.puesto:<15} ${empleado.salario:<10.2f}')

    elif opcion == 5:
        id_empleado = input("Ingrese el ID del empleado a eliminar: ")
        for i, empleado in enumerate(lista_empleados):
            if empleado.id_empleado == id_empleado:
                print(f"Se eliminará el empleado: {empleado.nombre} - {empleado.puesto}")
                
                
        else:
            print("Empleado no encontrado.")

    elif opcion == 6:
        print("Gracias. Hasta luego.")
        break

    else:
        print("Opción no válida, elige un número del 1 al 6.")