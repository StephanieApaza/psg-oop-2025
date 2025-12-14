# Definición
class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino
        self.en_minibus = False

    def subir(self, minibus):
        """El pasajero sube al minibus"""
        if self.destino in minibus.paradas_programadas:
            if not self.en_minibus:
                minibus.agregar_pasajero(self)
                self.en_minibus = True
                print(f"{self.nombre} subió al minibus {minibus.numero_ruta}")
        else:
            print(f"{self.nombre} no puede subir: su destino no está en el recorrido.")

    def bajar(self, minibus):
        """El pasajero baja del minibus"""
        if self.en_minibus and minibus.parada_actual == self.destino:
            minibus.retirar_pasajero(self)
            self.en_minibus = False
            print(f"{self.nombre} bajó en {self.destino}")
        else:
            print(f"{self.nombre} aún no llegó a su destino.")

class Minibus:
    def __init__(self, numero_ruta, paradas_programadas):
        self.numero_ruta = numero_ruta
        self.paradas_programadas = paradas_programadas
        self.pasajeros = []
        self.parada_actual = paradas_programadas[0]
        self.sentido_ruta = 1

    def avanzar_parada(self):
        """Simula el movimiento entre paradas circulares"""
        # Indice de la parada actual
        indice_actual_parada = self.paradas_programadas.index(self.parada_actual)

        # Próxima parada según el sentido 1 para seguir adelante y -1 para cambiar
        indice_siguiente_parada = indice_actual_parada + self.sentido_ruta

        # Cambiar de sentido si llega al final o al inicio
        if indice_siguiente_parada >= len(self.paradas_programadas):
            self.sentido_ruta *= -1
            indice_siguiente_parada = len(self.paradas_programadas) - 2
        elif indice_siguiente_parada < 0:
            self.sentido_ruta = 1
            indice_siguiente_parada = 1

        self.parada_actual = self.paradas_programadas[indice_siguiente_parada]
        print(f"Minibus {self.numero_ruta} llegó a la parada: {self.parada_actual}")

    def agregar_pasajero(self, pasajero):
        """Agrega un pasajero al minibus"""
        if pasajero not in self.pasajeros:
            self.pasajeros.append(pasajero)

    def retirar_pasajero(self, pasajero):
        """Disminuye un pasajero del minibus"""
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)

# Uso
# Lista de paradas
paradas = ["Arce", "Prado", "Perez"]

ruta_minibus = Minibus(723, paradas)

# Pasajeros
pasajero_amalia = Pasajero("Amalia", "Prado")
pasajero_luis = Pasajero("Luis", "Perez")
pasajero_marcela = Pasajero("Marcela", "Arce")
print("---------------------------------------------------------")
# Los pasajeros suben al minibus
pasajero_amalia.subir(ruta_minibus)
pasajero_luis.subir(ruta_minibus)
pasajero_marcela.subir(ruta_minibus)

print(f"Minibus {ruta_minibus.numero_ruta} inicia en la parada: {ruta_minibus.parada_actual}")
# Simular el recorrido
for numero_recorridos in range(4):
    print("---------------------------------------------------------")
    ruta_minibus.avanzar_parada()
    for pasajero in ruta_minibus.pasajeros[:]:
        pasajero.bajar(ruta_minibus)
