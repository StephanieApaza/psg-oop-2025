# Definición
class Pasajero:
    def __init__(self, nombre, ubicacion_destino):
        self.nombre = nombre
        self.ubicacion_destino = ubicacion_destino
        self.en_minibus = False

    def subir_minibus(self, minibus):
        """El pasajero sube al minibus"""
        if self.ubicacion_destino in minibus.lista_paradas:
            if not self.en_minibus:
                minibus.subir_pasajero(self)
                self.en_minibus = True
                print(f"{self.nombre} subió al minibus {minibus.numero_ruta}")
        else:
            print(f"{self.nombre} no puede subir: su destino no está en el recorrido.")

    def bajar_minibus(self, minibus):
        """El pasajero baja del minibus"""
        if self.en_minibus and minibus.parada_actual == self.ubicacion_destino:
            minibus.bajar_pasajero(self)
            self.en_minibus = False
            print(f"{self.nombre} bajó en {self.ubicacion_destino}")
        else:
            print(f"{self.nombre} no puede bajar en {minibus.parada_actual} le falta llegar a su destino.")
class Minibus:
    def __init__(self, numero_ruta, lista_paradas):
        self.numero_ruta = numero_ruta
        self.lista_paradas = lista_paradas
        self.pasajeros = []
        self.parada_actual = lista_paradas[0]
        self.sentido_ruta = 1

    def seguir_recorrido(self):
        """Simula el movimiento entre paradas circulares"""
        # Indice de la parada actual
        parada_indice_actual = self.lista_paradas.index(self.parada_actual)

        # Próxima parada según el sentido 1 para seguir adelante y -1 para cambiar
        parada_indice_siguiente = parada_indice_actual + self.sentido_ruta

        # Cambiar de sentido si llega al final o al inicio
        if parada_indice_siguiente >= len(self.lista_paradas):
            self.sentido_ruta *= -1
            parada_indice_siguiente = len(self.lista_paradas) - 2
        elif parada_indice_siguiente < 0:
            self.sentido_ruta = 1
            parada_indice_siguiente = 1

        self.parada_actual = self.lista_paradas[parada_indice_siguiente]
        print(f"Minibus {self.numero_ruta} llegó a la parada: {self.parada_actual}")

    def subir_pasajero(self, pasajero):
        """Agrega un pasajero al minibus"""
        if pasajero not in self.pasajeros:
            self.pasajeros.append(pasajero)

    def bajar_pasajero(self, pasajero):
        """Disminuye un pasajero del minibus"""
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)

# Uso
# Lista de paradas
paradas = ["Arce", "Prado", "Perez"]

minibus1 = Minibus(723, paradas)

# Pasajeros
pasajero1 = Pasajero("Amalia", "Prado")
pasajero2 = Pasajero("Luis", "Perez")
pasajero3 = Pasajero("Marcela", "Arce")
print("---------------------------------------------------------")
# Los pasajeros suben al minibus
pasajero1.subir_minibus(minibus1)
pasajero2.subir_minibus(minibus1)
pasajero3.subir_minibus(minibus1)

print(f"Minibus {minibus1.numero_ruta} inicia en la parada: {minibus1.parada_actual}")
# Simular el recorrido
for recorrido in range(4):
    print("---------------------------------------------------------")
    minibus1.seguir_recorrido()
    for pasajero in minibus1.pasajeros[:]:
        pasajero.bajar_minibus(minibus1)
