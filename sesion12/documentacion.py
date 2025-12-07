class Persona:
    """Clase persona de la sesion 12"""
    def __init__(self, nombre: str):
        """Inicializa el constructor
        Args:
            nombre (str): El nombre de la persona"""
        self.nombre: str = nombre
    def saludar(self) -> None:
        """Imprime el saludo con el nombre de la persona"""
        print(f"Hola, mi nombre es {self.nombre}")

jhon = Persona("Jhon")
jhon.saludar()
