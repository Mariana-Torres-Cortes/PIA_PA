class Calificaciones:
    def __init__(self, nombre, matricula, carrera, calificaciones): 
        self.nombre = nombre 
        self.matricula = matricula 
        self.carrera = carrera 
        
        self.calificaciones = list(map(float, calificaciones)) if calificaciones else []

    def informacion(self): 
        print(f"Nombre: {self.nombre}, Matricula: {self.matricula}, Carrera: {self.carrera}, Calificaciones: {self.calificaciones}")


lista_alumnos = [] 

while True:
    print("--- Menú ---")
    print("1. Agregar Alumno")
    print("2. Mostrar la información de un alumno")
    print("3. Modificar alumno")
    print("4. Mostrar todos los alumnos")
    print("5. Eliminar alumno")
    print("6. Salir")

    try:
        opcion = int(input("¿Qué opción desea realizar?: ").strip())
    except ValueError:
        print("Opción inválida, escribe un número del 1 al 6.")
        continue

    if opcion == 1: 
        nombre = input("¿Cuál es el nombre? ")
        matricula = input("¿Cuál es la matrícula? ")
        carrera = input("¿Cuál es la carrera? ")
        calificaciones = input("Introduce las calificaciones separadas por comas: ").split(",")

        nuevo_alumno = Calificaciones(nombre, matricula, carrera, calificaciones)
        lista_alumnos.append(nuevo_alumno)
        print("Nuevo alumno guardado.")  

    elif opcion == 2: 
        matricula = input("Ingrese la matrícula del alumno: ")
        encontrado = False
        for alumno in lista_alumnos:
            if alumno.matricula == matricula:
                alumno.informacion()
                promedio = sum(alumno.calificaciones) / len(alumno.calificaciones) if alumno.calificaciones else 0
                print(f"Promedio: {promedio:.2f}")
                encontrado = True
                break
        if not encontrado:
            print("Alumno no encontrado.") 

    elif opcion == 3: 
        matricula = input("Ingrese la matrícula del alumno a modificar: ")
        for alumno in lista_alumnos:
            if alumno.matricula == matricula:
                print("Datos actuales:")
                alumno.informacion()

                alumno.nombre = input("Nuevo nombre (Enter para no cambiar): ") or alumno.nombre
                alumno.carrera = input("Nueva carrera (Enter para no cambiar): ") or alumno.carrera
                nuevas_calificaciones = input("Nuevas calificaciones separadas por comas (dejar vacío para no cambiar): ")
                if nuevas_calificaciones:
                    alumno.calificaciones = list(map(float, nuevas_calificaciones.split(",")))

                print("Datos actualizados.")
                break
        else:
            print("Alumno no encontrado.")

    elif opcion == 4:
        if not lista_alumnos:
            print("No hay alumnos registrados.")
        else:
            print("\nLista de Alumnos:")
            print(f'{"Matrícula":<10} {"Nombre":<15} {"Carrera":<15} {"Promedio":<8}')
            for alumno in lista_alumnos:
                promedio = sum(alumno.calificaciones) / len(alumno.calificaciones) if alumno.calificaciones else 0
                print(f'{alumno.matricula:<10} {alumno.nombre:<15} {alumno.carrera:<15} {promedio:<8.2f}') 

    elif opcion == 5:
        matricula = input("Ingrese la matrícula del alumno a eliminar: ")
        for i, alumno in enumerate(lista_alumnos):
            if alumno.matricula == matricula:
                print(f"Se eliminará el alumno: {alumno.nombre} - {alumno.carrera}")
                confirmar = input("¿Está seguro? (S/N): ")
                if confirmar.upper() == "S":
                    lista_alumnos.pop(i)
                    print("Alumno eliminado.")
                break
        else:
            print("Alumno no encontrado.") 

    elif opcion == 6:
        print(" Gracias por su visita. Hasta luego.")
        break  

    else:
        print(" Opción no válida, elige un número del 1 al 6.")

        


    



              