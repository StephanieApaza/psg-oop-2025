# Definición
class Cidra():
    def __init__(self, acidez, cascara):
        self.acidez = acidez
        self.cascara = cascara

class Naranja():
    def __init__(self, dulzura, jugosidad):
        self.dulzura = dulzura
        self.jugosidad = jugosidad

class Limon(Cidra, Naranja):
    def __init__(self, acidez, cascara, dulzura, jugosidad):
        Cidra.__init__(self, acidez, cascara)
        Naranja.__init__(self, dulzura, jugosidad)

# Ejemplo de uso
cidra = Cidra("alta", "dura")
naranja = Naranja("media", "jugosa")
limon = Limon("alta", "dura", "baja", "media")

print(f"Cidra => Acidez: {cidra.acidez}")
print(f"Cáscara: {cidra.cascara}")

print(f"Naranja => Dulzura: {naranja.dulzura}")
print(f"Jugosidad: {naranja.jugosidad}")

print(f"Limón => Acidez: {limon.acidez}")
print(f"Cáscara: {limon.cascara}")
print(f"Dulzura: {limon.dulzura}")
print(f"Jugosidad: {limon.jugosidad}")
