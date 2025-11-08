# Definición
class Martillo:
    def __init__(self, tipo_mango, material, peso):
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso

    def usar(self):
        """Simula el uso del martillo"""
        print("Usando el martillo para clavar clavos.")

class Destornillador:
    def __init__(self, tipo_mango, material, tamano_punta):
        self.tipo_mango = tipo_mango
        self.material = material
        self.tamano_punta = tamano_punta

    def usar(self):
        """Simula el uso del destornillador"""
        print("Usando el destornillador para ajustar tornillos.")

class LlaveInglesa:
    def __init__(self, tipo_mango, material, medida_ajuste):
        self.tipo_mango = tipo_mango
        self.material = material
        self.medida_ajuste = medida_ajuste

    def usar(self):
        """Simula el uso de la llave inglesa"""
        print("Usando la llave inglesa para apretar tuercas.")

class Carpintero:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self, herramienta):
        """El carpintero trabaja con cualquier herramienta que tenga el método usar()"""
        print(f"{self.nombre} comienza a trabajar...")
        herramienta.usar()
        print(f"{self.nombre} terminó de usar la herramienta.\n")

# Uso
martillo = Martillo("madera", "acero", 1.5)
destornillador = Destornillador("plástico", "acero", "estrella")
llave_inglesa = LlaveInglesa("goma", "metal", "15mm")
carpintero = Carpintero("Luis")

# El carpintero usa diferentes herramientas sin importar su tipo
carpintero.trabajar(martillo)
carpintero.trabajar(destornillador)
carpintero.trabajar(llave_inglesa)