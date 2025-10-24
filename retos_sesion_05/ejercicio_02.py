# Definición
class Nadador():
    def nadar(self):
        """Acción de desplazarse en el agua"""
        print(f"Estoy nadando en el agua.")

class Volador():
    def volar(self):
        """Acción de desplazarse por el aire"""
        print(f"Estoy volando por el cielo.")

class Pez(Nadador):
    def mostrar(self):
        print(f"Soy pez 🐠 y mi habilidad es nadar.")
        self.nadar()

class Pajaro(Volador):
    def mostrar(self):
        print(f"Soy pájaro 🦅 y mi habilidad es volar.")
        self.volar()

class Pato(Nadador, Volador):
    def mostrar(self):
        print(f"Soy pato 🦆 y mi habilidad combinada es nadar y volar.")
        self.nadar()
        self.volar()

# Ejemplo de uso
personaje1 = Pez()
personaje2 = Pajaro()
personaje3 = Pato()
print("--------------------------------------------------------")
personaje1.mostrar()
print("--------------------------------------------------------")
personaje2.mostrar()
print("--------------------------------------------------------")
personaje3.mostrar()