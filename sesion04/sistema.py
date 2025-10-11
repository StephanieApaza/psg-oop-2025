# Definiendo la clase
class SistemaOperativo:
    def __init__(self, nombre, fondo_pantalla, reloj):
        self.nombre = nombre
        self.fondo_pantalla = fondo_pantalla
        self._reloj = reloj
        self.__bateria = 1 # nivel privado
        self.__pin = '0000' # privado

    def cambiar_fondo_pantalla(self, imagen):
        self.fondo_pantalla = imagen
        print(f"Nuevo fondo: {self.fondo_pantalla}")
        return self.fondo_pantalla
    
    def ver_hora(self):
        print(f"La hora actual es: {self._reloj}")
        return self._reloj
    
    def estado_bateria(self):
        print(f"El estado de la bateria es: {self.__bateria}%")
        return self.__bateria
    
    def cargador(self, cantidad):
        print("Cargador conectado")
        self.__bateria += cantidad
        print(f"Bateria cargada a: {self.__bateria}%")
        print("Cargador desconectado")

    def cambiar_pin(self, nuevo_pin):
        self.__pin = nuevo_pin
        print(f"Pin cambiado exitosamente")

# Implementando la clase
so = SistemaOperativo("PyPhoneOS", "gatitos.jpg", "15:44")
print(f"Fondo de pantalla: {so.fondo_pantalla}")
so.cambiar_fondo_pantalla("perritos.jpg")
so.fondo_pantalla = "paisajes.jpg"  # Cambiando directamente
print(f"Fondo de pantalla: {so.fondo_pantalla}")
so.ver_hora()
# print(f"Reloj: {so._reloj}") # NO RECOMENDADO
so.estado_bateria()
so.cargador(20)
so.estado_bateria()
so.cambiar_pin('4538')
try:
    print(f"Batería: {so.__bateria}")  # Error
except AttributeError as e:
    print(f"Error: {e}")

