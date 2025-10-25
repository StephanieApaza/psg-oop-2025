# Definición
class Corazon:
    def __init__(self, peso, tamano):
        self.contraido = False
        self.puede_latir = True
        self.peso = peso
        self.tamano = tamano

    def latir(self):
        if self.puede_latir:
            if self.contraido:
                print("❤️  Diástole: Corazón relajandose")
            else:
                print("❤️  Sístole: Corazón contrayendose")
            self.contraido = not self.contraido

    def info(self):
        estado = "Contraído" if self.contraido else "Relajado"
        print(f"Corazón: {self.peso} kg, {self.tamano} cm")
        print(f"Estado: {estado} Puede latir: {self.puede_latir}")

class Cerebro:
    def __init__(self, peso):
        self.peso = peso

    def pensar(self):
        print("🧠 Pensando...")

    def info(self):
        print(f"Cerebro: {self.peso} kg")

class Cuerpo:
    def __init__(self, nombre, peso_corazon, tamano_corazon):
        self.nombre = nombre
        self.corazon = Corazon(peso_corazon, tamano_corazon)
        self.cerebro = Cerebro(1.4)

    def info(self):
        print(f"Cuerpo: {self.nombre}")
        self.corazon.info()
        self.cerebro.info()

    def vivir(self):
        if self.corazon.puede_latir:
            self.corazon.latir()
            self.cerebro.pensar()
            print(f"{self.nombre} está vivo")
        else:
            print(f"{self.nombre} esta muerto")

# Uso
cuerpo = Cuerpo("Jhon", 0.3, 12)
cuerpo.info()
cuerpo.vivir()
cuerpo.vivir()