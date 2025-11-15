# Definición
class Libro:
    def __init__(self, titulo, autor):  # Constructor
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"({self.titulo} - {self.autor})"

class Biblioteca:
    def __init__(self):  # Constructor
        self.libros = []  # Colección de libros
    def __str__(self):
        return ', '.join(str(libro) for libro in self.libros) 
    def __len__(self):  # Método de longitud
        return len(self.libros)
    def __getitem__(self, indice):  # Obtención de elementos
        return self.libros[indice]
    def __setitem__(self, indice, valor):  # Asignación de elementos
        self.libros[indice] = valor
    def __delitem__(self, indice):  # Eliminación de elementos
        del self.libros[indice]
    def __iter__(self):  # Iterador
        return iter(self.libros)

# Uso
biblioteca = Biblioteca()
biblioteca.libros.append(Libro("1984", "George Orwell"))
biblioteca.libros.append(Libro("La odisea", "Homero"))
print(biblioteca)
longiud = len(biblioteca)  # Obtener la longitud 
print(f"Número de libros: {longiud}")
libro = biblioteca[0]  # Acceder al primer libro
print(libro)
biblioteca[1] = Libro("Don Quijote", "Miguel de Cervantes")
print(biblioteca)
for libro in biblioteca:  # Iterar sobre los libros
    print(libro)
del biblioteca[0]  # Eliminar el primer libro
print(biblioteca)