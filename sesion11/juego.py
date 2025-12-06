import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def elegir(self):
        eleccion = input(f"{self.nombre}, elige piedra, papel o tijera: ").lower()
        while eleccion not in ["piedra", "papel", "tijera"]:
            eleccion = input("Opción inválida. Intenta de nuevo: ").lower()
        return eleccion

class Computadora:
    def __init__(self):
        self.nombre = "Computadora"

    def elegir(self):
        return random.choice(["piedra", "papel", "tijera"])

class Juego:
    def __init__(self, jugador, computadora):
        self.jugador = jugador
        self.computadora = computadora

    def determinar_ganador(self, eleccion_jugador, eleccion_computadora):
        if eleccion_jugador == eleccion_computadora:
            return "Empate"
        elif (
            (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or
            (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or
            (eleccion_jugador == "tijera" and eleccion_computadora == "papel")
        ):
            return f"{self.jugador.nombre} gana!"
        else:
            return f"{self.computadora.nombre} gana!"

    def jugar(self):
        eleccion_jugador = self.jugador.elegir()
        eleccion_computadora = self.computadora.elegir()

        print(f"{self.jugador.nombre} eligió: {eleccion_jugador}")
        print(f"{self.computadora.nombre} eligió: {eleccion_computadora}")

        resultado = self.determinar_ganador(eleccion_jugador, eleccion_computadora)
        print(resultado)

print("🎮 Bienvenido al juego de Piedra, Papel o Tijera")
nombre = input("Introduce tu nombre: ")
jugador = Jugador(nombre)
computadora = Computadora()
juego = Juego(jugador, computadora)

while True:
    print("\n--- Menú ---")
    print("1. Jugar")
    print("2. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        juego.jugar()
    elif opcion == "2":
        print("¡Gracias por jugar! 👋")
        break
    else:
        print("Opción inválida, intenta de nuevo.")