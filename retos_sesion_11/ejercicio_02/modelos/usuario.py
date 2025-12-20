class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def solicitar_prestamo(self, libro, biblioteca):
        if libro in biblioteca.libros_disponibles:
            self.libros_prestados.append(libro)
            biblioteca.prestar_libro(libro, self)
            print(f"Libro '{libro.titulo}' prestado a {self.nombre}.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")

    def devolver_libros(self, biblioteca):
        if self.libros_prestados:
            biblioteca.devolver_prestamo(self)
            print(f"{self.nombre} devolvió todos los libros prestados.")
            self.libros_prestados.clear()
        else:
            print(f"{self.nombre} no tiene libros prestados.")