from modelos import Libro, Usuario

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []
        self.prestamos = []  # Lista de tuplas (usuario, libro)

    def registrar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Libro '{libro.titulo}' registrado en la biblioteca.")

    def listar_libros(self):
        if not self.libros_disponibles:
            print("No hay libros disponibles.")
        else:
            print("Libros disponibles:")
            for indice_libro, libro in enumerate(self.libros_disponibles, start=1):
                print(f"{indice_libro}. {libro}")

    def prestar_libro(self, libro, usuario):
        if libro in self.libros_disponibles:
            self.libros_disponibles.remove(libro)
            self.registrar_prestamo(usuario, libro)

    def registrar_prestamo(self, usuario, libro):
        self.prestamos.append((usuario, libro))

    def devolver_prestamo(self, usuario):
        prestamos_del_usuario = [
            (usuario_prestamo, libro_prestado) 
            for usuario_prestamo, libro_prestado in self.prestamos
            if usuario_prestamo == usuario
        ]
        for _, libro_prestado in prestamos_del_usuario:
            self.libros_disponibles.append(libro_prestado)
        self.prestamos = [
            (usuario_prestamo, libro_prestado) 
            for usuario_prestamo, libro_prestado in self.prestamos
            if usuario_prestamo != usuario
        ]

    def mostrar_prestamos(self):
        if not self.prestamos:
            print("No hay libros prestados actualmente.")
        else:
            print("Libros prestados:")
            for usuario_prestamo, libro_prestado in self.prestamos:
                print(f"{libro_prestado} -> Prestado a {usuario_prestamo.nombre}")