from random import choice
from constantes import OPCIONES

class Computadora:
    def __init__(self):
        self.nombre = "CPU"

    def __str__(self):
        return self.nombre

    def elegir(self):
        return choice(OPCIONES)