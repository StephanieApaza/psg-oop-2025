# Definición
class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def info(self):
        print (f"Título:{self.titulo}\nAutor:{self.autor}\nGénero:{self.genero}")

class Periodico:
    def __init__(self, dia, mes, gestion, editorial):
        self.dia = dia
        self.mes = mes
        self.gestion = gestion
        self.editorial = editorial

    def info(self):
        print (f"Periódico:{self.editorial}\nFecha:{self.dia}/{self.mes}/{self.gestion}")

class Librero:
    def __init__(self, genero):
        self.genero = genero
        self.libros = []  # Lista de libros
        self.periodicos = [] # Lista de periodicos

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def eliminar_libro(self, libro):
        if libro not in self.libros:
            print("El libro no está en el librero")
            return
        print(f"❌ Libro eliminado: {libro.titulo}")
        self.libros.remove(libro)

    def mostrar_libros(self):
        print(f"📘 Librero de {self.genero}")
        for libro in self.libros:
            libro.info()

    def agregar_periodico(self, periodico):
        self.periodicos.append(periodico)

    def eliminar_periodico(self, periodico):
        if periodico not in self.periodicos:
            print("El periódico no está en el librero")
            return
        print(f"❌ Periódico eliminado: {periodico.editorial} {periodico.dia}/{periodico.mes}/{periodico.gestion}")
        self.periodicos.remove(periodico)

    def mostrar_periodicos(self):
        print(f"📰 Periódicos de librero de {self.genero}")
        for periodico in self.periodicos:
            periodico.info()

# Uso
librero_cocina = Librero("Cocina")
libro1 = Libro("Cocina Criolla Boliviana", "Daniel Figliuzzi", "Cocina")
libro2 = Libro("Gran libro cocina Boliviana", "Jaime Cisneros", "Cocina")
librero_cocina.agregar_libro(libro1)
librero_cocina.agregar_libro(libro2)
librero_cocina.mostrar_libros()

librero_arte = Librero("Arte")
libro3 = Libro("Arte textil y mundo andino", "Teresa Gisbert", "Arte")
libro4 = Libro("Arte contemporáneo en Bolivia", "Galería Altamira", "Arte")
librero_arte.agregar_libro(libro3)
librero_arte.agregar_libro(libro4)
librero_arte.mostrar_libros()

librero_cocina.eliminar_libro(libro1)
librero_cocina.mostrar_libros()
libro1.info()

periodico1 = Periodico(1, 1, 2020, "La Prensa")
periodico2 = Periodico(2, 1, 2020, "El Deber")
librero_cocina.agregar_periodico(periodico1)
librero_cocina.agregar_periodico(periodico2)
librero_cocina.mostrar_periodicos()
librero_cocina.eliminar_periodico(periodico1)
librero_cocina.mostrar_periodicos()