def guardar_tarea():
    tarea = input("Escribe una nueva tarea: ")
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")
    print("Tarea guardada.")

def ver_tareas():
    print("\nTus tareas:")
    try:
        with open("tareas.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("Aún no hay tareas guardadas.")

print("---- GESTOR DE TAREAS ----")
print("1. Agregar nueva tarea")
print("2. Ver tareas")

opcion = input("Selecciona una opción (1 o 2): ")

if opcion == "1":
    guardar_tarea()
elif opcion == "2":
    ver_tareas()
else:
    print("Opción no válida.")