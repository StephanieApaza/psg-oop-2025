import random

class PiedraPapelTijera:
    __instancia = None
    iniciado = False

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia
    
    def __init__(self):
        if self.iniciado:
            print("El juego ya está en curso.")
            return
        self.__puntaje_jugador = 0
        self.__puntaje_computadora = 0

    def iniciar_partida(self):
        opciones = ["piedra", "papel", "tijera"]
        eleccion_jugador = input("Elige piedra, papel o tijera: ").lower().strip()

        if eleccion_jugador not in opciones:
            print("❎ Opción inválida. Intenta elegir piedra, papel o tijera.")
            return
        
        eleccion_computadora = random.choice(opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_jugador == eleccion_computadora:
            print("🤝 ¡Empate!")
        elif (
            (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or
            (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or
            (eleccion_jugador == "tijera" and eleccion_computadora == "papel")
        ):
            print("🎉 ¡Ganaste la ronda!")
            self.__puntaje_jugador += 1
        else:
            print("La computadora gana la ronda.")
            self.__puntaje_computadora += 1

    def mostrar_puntaje(self):
        print("\nPuntajes:")
        print(f"Jugador: {self.__puntaje_jugador}")
        print(f"Computadora: {self.__puntaje_computadora}\n")

    def reiniciar_juego(self):
        self.__puntaje_jugador = 0
        self.__puntaje_computadora = 0
        print("🔄 Juego reiniciado: Puntajes reiniciados a cero.\n")

# Menú
juego = PiedraPapelTijera()

while True:
    print("\nMENÚ")
    print("1. Iniciar una nueva partida")
    print("2. Mostrar puntajes")
    print("3. Reiniciar puntajes")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        juego.iniciar_partida()
    elif opcion == "2":
        juego.mostrar_puntaje()
    elif opcion == "3":
        juego.reiniciar_juego()
    elif opcion == "4":
        print("👋 Saliendo del juego... ¡Gracias por jugar!")
        break
    else:
        print("❎ Opción inválida.")