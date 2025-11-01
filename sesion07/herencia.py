# Definición
class Vehiculo:
    def __init__(self, tipo, energia):
        self.tipo = tipo
        self.energia = energia
    
    def moverse(self):
        print(f"El vehículo {self.tipo}")
        print(f"Se mueve con {self.energia}")

class Auto(Vehiculo):
    def __init__(self):
        super().__init__("Terrestre", "motor a gasolina")
    
    def moverse(self):
        print("El 🚗 avanza a 200 km/h")
        print(f"Utiliza {self.energia} y es {self.tipo}")

class Bicicleta(Vehiculo):
    def __init__(self):
        super().__init__("Terrestre", "pedales")
    
    def moverse(self):
        print("La 🚲 avanza a 20 km/h")
        print(f"Es {self.tipo} y {self.energia}")

class Avion(Vehiculo):
    def __init__(self):
        super().__init__("Aéreo", "motor a gasolina")

    def moverse(self):
        print("El ✈️  avanza a 900 km/h")
        print(f"Utiliza {self.energia} y es {self.tipo}")

class Bote(Vehiculo):
    def __init__(self):
        super().__init__("Acuático", "viento")
    
    def moverse(self):
        print("El ⛵ navega a 30 km/h")
        print(f"Utiliza {self.energia} y es {self.tipo}")

# Uso
auto = Auto()
bicicleta = Bicicleta()
avion = Avion()
bote = Bote()
auto.moverse()
bicicleta.moverse()
avion.moverse()
bote.moverse()