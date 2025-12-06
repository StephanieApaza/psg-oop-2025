from constantes import OPCIONES

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre
    
    def ingresar(self, mensaje):
        return input(f"{self}, {mensaje}: ").lower()

    def validar_eleccion(self, eleccion):
        while eleccion not in OPCIONES:
            eleccion = self.ingresar("opción inválida. Intenta de nuevo")
        return eleccion

    def elegir(self):
        opciones = ", ".join(OPCIONES)
        eleccion = self.ingresar(f"elige {opciones}")
        return self.validar_eleccion(eleccion)