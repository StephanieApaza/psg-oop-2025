# Definiendo la clase
class Edificio:
    def __init__(self):
        self.__pin = '1234' 
        self.__telefono = "123-456-7890" 

    @property
    def pin(self):  
        return self.__pin
    
    @pin.setter
    def pin(self, nuevo_pin): 
        if len(str(nuevo_pin)) == 4:
            self.__pin = nuevo_pin
            print("Pin cambiado exitosamente.")
        else:
            print("El pin debe ser número de 4 dígitos.")

    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono
        print("Número telefónico cambiado exitosamente.")

# Implementando la clase
edificio = Edificio()
print(f"Pin actual: {edificio.pin}")
edificio.pin = '56789'  # Error
edificio.pin = '5678'   # Correcto
print(f"Pin actualizado: {edificio.pin}")
print(f"# telefónico actual: {edificio.telefono()}")
edificio.telefono("098-765-4321")
print(f"# telefónico actualizado: {edificio.telefono()}")