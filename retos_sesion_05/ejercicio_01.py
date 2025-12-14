# Definición
class Vehiculo():
    def __init__(self, velocidad, medio):
        self._velocidad = velocidad
        self.medio = medio

    @property
    def velocidad(self):
        return self._velocidad

    def mostrar_datos(self):
        """Información general del vehículo"""
        print(f"Medio: {self.medio}")
        print(f"Velocidad actual: {self._velocidad} km/h")

class Bicicleta(Vehiculo):
    def __init__(self, velocidad, medio = "terrestre"):
        super().__init__(velocidad, medio)

    def pedalear(self):
        """Aumenta la velocidad al pedalear"""
        self._velocidad += 7
        print(f"La bicicleta esta pedaleando. Su velocidad actual es: {self._velocidad} km/h")

class Avion(Vehiculo):
    def __init__(self, velocidad, medio = "aereo"):
        super().__init__(velocidad, medio)

    def volar(self):
        """Aumenta la velocidad al volar"""
        self._velocidad += 70
        print(f"El avión esta volando. Su velocidad actual es: {self._velocidad} km/h")

# Ejemplo de uso
bicicleta_urbana = Bicicleta(1)
avion_comercial= Avion(100)
print("-------------------------------------------------")
# Datos iniciales
bicicleta_urbana.mostrar_datos()
avion_comercial.mostrar_datos()
print("-------------------------------------------------")
# Acciones
bicicleta_urbana.pedalear()
avion_comercial.volar()