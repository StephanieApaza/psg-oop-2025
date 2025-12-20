from models.lista_tareas import ListaTareas

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Eliminar tareas completadas")
    print("6. Eliminar todas las tareas")
    print("7. Salir")

def main():
    lista_tareas = ListaTareas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_tareas.agregar_tarea(descripcion)

        elif opcion == "2":
            lista_tareas.mostrar_tareas()

        elif opcion == "3":
            lista_tareas.mostrar_tareas()
            indice = int(input("Ingrese el índice: "))
            lista_tareas.completar_tarea(indice)

        elif opcion == "4":
            lista_tareas.mostrar_tareas()
            indice = int(input("Ingrese el índice: "))
            lista_tareas.eliminar_tarea(indice)

        elif opcion == "5":
            lista_tareas.eliminar_tareas_completadas()

        elif opcion == "6":
            lista_tareas.eliminar_todas()

        elif opcion == "7":
            print("¡Gracias por usar la aplicación! 👋")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()