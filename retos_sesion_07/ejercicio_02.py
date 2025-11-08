# Definición
class Instrumento:
    def __init__(self, nombre, material):
        self._nombre = nombre
        self._material = material

    def tocar(self):
        print("El instrumento está produciendo un sonido.")

class Guitarra(Instrumento):
    def __init__(self, nombre, material, numero_cuerdas, tipo):
        super().__init__(nombre, material)
        self._numero_cuerdas = numero_cuerdas
        self._tipo = tipo

    def tocar(self):
        print(f"La guitarra 🎸 hace 'strum' ({self._numero_cuerdas} cuerdas, tipo {self._tipo})")

class Piano(Instrumento):
    def __init__(self, nombre, material, numero_teclas, tipo):
        super().__init__(nombre, material)
        self._numero_teclas = numero_teclas
        self._tipo = tipo

    def tocar(self):
        print(f"El piano 🎹 hace 'plin' ({self._numero_teclas} teclas, tipo {self._tipo})")

class Tambor(Instrumento):
    def __init__(self, nombre, material, tipo_percusion, diametro):
        super().__init__(nombre, material)
        self._tipo_percusion = tipo_percusion
        self._diametro = diametro

    def tocar(self):
        print(f"El tambor 🥁 hace 'boom' (tipo {self._tipo_percusion}, diámetro {self._diametro} cm)")

# Uso
guitarra = Guitarra("Guitarra acústica", "madera", 6, "acústica")
piano = Piano("Piano clásico", "madera", 50, "de cola")
tambor = Tambor("Tambor tradicional", "cuero", "percusión de mano", 30)

instrumentos = [guitarra, piano, tambor]

def practicar_instrumentos(instrumentos):
    """El usuario practica con distintos instrumentos sin importar su tipo"""
    print("El usuario comienza a practicar...\n")
    for instrumento in instrumentos:
        instrumento.tocar()
    print("\nFin de la práctica musical.")

practicar_instrumentos(instrumentos)
