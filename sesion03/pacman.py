class Pacman:
    max_vidas = 2
    def __init__(self):
        self.puntaje = 0
        self.vidas = self.max_vidas

    @classmethod # Método de clase
    def jugar(cls):
        print("Pacman ha nacido")
        return cls
    
    def comer_punto(self, punto): # Método de instancia
        self.puntaje += punto
        print(f"Pacman ha comido un punto de valor {punto}")
        print(f"Puntaje actual: {self.puntaje}")

    def morir(self): # Método de instancia
        if self.vidas > 0:
            self.vidas -= 1
            print(f"Pacman ha muerto, quedan {self.vidas} vidas")
        else:
            print("Pacman no tiene más vidas") 
    
    def juego_terminado(self): # Método de instancia
        if self.vidas == 0:
            print("El juego ha terminado")
            return True
        else:
            print("Pacman tiene vidas restantes")
            return False

    @staticmethod # Nuevo Método estático
    def calcular_record(actual, nuevo):
        if nuevo > actual:
            print("¡Nuevo record!")
            return nuevo
        else:
            print("No hay nuevo record")
            return actual
        
# Instanciando un objeto
record = 0
pacman = Pacman.jugar()
pacman.comer_punto(1)
pacman.comer_punto(2)
pacman.morir()
pacman.morir()
pacman.morir()
if pacman.juego_terminado():
    record = Pacman.calcular_record(record, pacman.puntaje)
    print(f"Record actual: {record}")
else:
    print("Pacman sigue jugando")
pacman_2 = Pacman.jugar()
pacman_2.comer_punto(1)
pacman_2.morir()
pacman_2.morir()
if pacman_2.juego_terminado():
    record = Pacman.calcular_record(record, pacman_2.puntaje)
    print(f"Record actual: {record}")
else:
    print("Pacman sigue jugando")
