import random

class DadosDeLaSuerte:
    """Clase que representa el juego Dados de la Suerte."""

    def __init__(self) -> None:
        """Inicializa el juego con estado y último lanzamiento."""
        self.ultimo_lanzamiento: int = 0
        self.estado_juego: str = ""
        self.continuar_juego: bool = True

    def lanzar_dados(self) -> int:
        """Lanza dos dados y devuelve la suma."""
        dado_uno: int = random.randint(1, 6)
        dado_dos: int = random.randint(1, 6)
        self.ultimo_lanzamiento = dado_uno + dado_dos
        return self.ultimo_lanzamiento

    def evaluar_lanzamiento(self) -> None:
        """Evalúa el último lanzamiento y actualiza el estado del juego."""
        if self.ultimo_lanzamiento in [7, 11]:
            self.estado_juego = "¡Ganaste 🎉!"
            self.continuar_juego = False
        elif self.ultimo_lanzamiento in [2, 3, 12]:
            self.estado_juego = "Perdiste, vuelve a intentarlo. 😣"
            self.continuar_juego = False
        else:
            self.estado_juego = f"Puedes volver a lanzar, suma: {self.ultimo_lanzamiento}"
            self.continuar_juego = True

    def jugar(self) -> None:
        """Ejecuta el flujo completo del juego."""
        print("¡Bienvenido a Dados de la Suerte!\n")

        while self.continuar_juego:
            input("Presiona Enter para lanzar los dados.")
            lanzamiento: int = self.lanzar_dados()
            self.evaluar_lanzamiento()
            print(f"Lanzamiento: {lanzamiento} -> {self.estado_juego}")
            
            if self.continuar_juego:
                respuesta: str = input("¿Deseas lanzar otra vez? (SI/NO): ").strip().lower()
                if respuesta != "si":
                    print("Juego terminado. ¡Gracias por jugar!")
                    break
            else:
                print("Fin del juego. ¡Gracias por participar!")

if __name__ == "__main__":
    juego = DadosDeLaSuerte()
    juego.jugar()