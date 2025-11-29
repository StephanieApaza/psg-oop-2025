# Productos
class Arma:
    def atacar(self):
        print("Atacando con un arma")

class Espada(Arma):
    def atacar(self):
        print("⚔️  Atacando con una espada")

class Arco(Arma):
    def atacar(self):
        print("🏹  Atacando con un arco")

# Fabricas
class Herramienta:
    def fabricar(self):
        pass
class Martillo(Herramienta):
    def fabricar(self):
        return Espada()
class Sierra(Herramienta):
    def fabricar(self):
        return Arco()

# Clase del armero   
class Armero():
    def fabricar_arma(self, tipo):
        if tipo == "espada":
            return Martillo().fabricar()
        if tipo == "arco":
            return Sierra().fabricar()
        raise ValueError("Arma no disponible. Inténtelo de nuevo")


while True:
    tipo_arma = input("¿Qué arma desea? (espada/arco/salir): ")
    tipo_arma = tipo_arma.lower().strip()
    if tipo_arma == "salir":
        print("Saliendo del juego.")
        break
    try:
        armero = Armero()
        arma = armero.fabricar_arma(tipo_arma)
        arma.atacar()
    except ValueError as e:
        print(e)
