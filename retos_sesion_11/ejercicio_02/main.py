from modelos import Libro, Usuario
from logica import Biblioteca

def main():
    print("¡Bienvenido a la Biblioteca!\n")

    biblioteca = Biblioteca()

    # Registro inicial de libros
    biblioteca.registrar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez", "001"))
    biblioteca.registrar_libro(Libro("Encontrar Tu Por Qué", "Simon Sinek", "002"))
    biblioteca.registrar_libro(Libro("El Club de las 5AM", "Robin Sharma", "003"))

    usuarios = {}

    while True:
        nombre_usuario = input("Ingrese su nombre (o 'salir' para finalizar): ").strip()
        if nombre_usuario.lower() == "salir":
            print("Saliendo del sistema...")
            break

        if nombre_usuario not in usuarios:
            usuarios[nombre_usuario] = Usuario(nombre_usuario)
        usuario_actual = usuarios[nombre_usuario]

        while True:
            print("\nOpciones:")
            print("1. Listar libros disponibles")
            print("2. Solicitar préstamo de libro")
            print("3. Devolver todos los libros prestados")
            print("4. Mostrar préstamos activos")
            print("5. Salir al menú principal")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                biblioteca.listar_libros()
            elif opcion == "2":
                if not biblioteca.libros_disponibles:
                    print("No hay libros disponibles para prestar.")
                    continue
                seleccion = input("Ingrese el número del libro que desea prestar: ").strip()
                if seleccion.isdigit():
                    indice = int(seleccion) - 1
                    if 0 <= indice < len(biblioteca.libros_disponibles):
                        libro_seleccionado = biblioteca.libros_disponibles[indice]
                        usuario_actual.solicitar_prestamo(libro_seleccionado, biblioteca)
                    else:
                        print("Número de libro inválido.")
                else:
                    print("Ingrese un número válido.")
            elif opcion == "3":
                usuario_actual.devolver_libros(biblioteca)
            elif opcion == "4":
                biblioteca.mostrar_prestamos()
            elif opcion == "5":
                break
            else:
                print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main()