from constantes import REGLAS
class Juego:
    def __init__(self, jugador, computadora):
        self.jugador = jugador
        self.computadora = computadora

    def determinar_ganador(self, eleccion_jugador, eleccion_computadora):
        if eleccion_jugador == eleccion_computadora:
            return "Empate"
        if REGLAS[eleccion_jugador] == eleccion_computadora:
            return f"{self.jugador} gana!"
        return f"{self.computadora} gana!"
    
    def mostrar_elecciones(self, jugador, eleccion):
        print(f"{jugador} eligió: {eleccion}")

    def jugar(self):
        eleccion_jugador = self.jugador.elegir()
        eleccion_computadora = self.computadora.elegir()

        self.mostrar_elecciones(self.jugador,eleccion_jugador)
        self.mostrar_elecciones(self.computadora,eleccion_computadora)
        

        resultado = self.determinar_ganador(eleccion_jugador, eleccion_computadora)
        print(resultado)
