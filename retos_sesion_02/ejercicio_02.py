class Vino:
    def __init__(self, nombre, tipo, cepa, anio_produccion):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio_produccion = anio_produccion

print("Vinos registrados:")
Vino1 = Vino("Antinori Tignanello", "Tinto", "Sangiovenese con Cabernet", 2018)
Vino2 = Vino("Chateau", "Tinto", "Cabernet Sauvignon", 2015)
Vino3 = Vino("Cloudy Bay Sauvignon Blanc", "Blanco", "Sauvignon Blanc", 2021)
Vino4 = Vino("Moet & Chandon Imperial Brut", "Espumoso", "Pinot Noir y Meunier", 2010)

print("Vino 1: ", Vino1.nombre, Vino1.tipo, Vino1.cepa, Vino1.anio_produccion)
print("Vino 2: ", Vino2.nombre, Vino2.tipo, Vino2.cepa, Vino2.anio_produccion)
print("Vino 3: ", Vino3.nombre, Vino3.tipo, Vino3.cepa, Vino3.anio_produccion)
print("Vino 4: ", Vino4.nombre, Vino4.tipo, Vino4.cepa, Vino4.anio_produccion)

class Queso:
    def __init__(self, nombre, variedad, edad, lleva_sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad   # En meses
        self.lleva_sal = lleva_sal

print("\nQuesos registrados: ")
Queso1 = Queso("Roquefort", "Azul - de leche de vaca", 2, True)
Queso2 = Queso("Parmigiano-Reggiano", "Duro - de leche de vaca", 1, False)
Queso3 = Queso("Manchego", "Semicurado - de leche de oveja manchega", 3, True)

print("Queso 1: ", Queso1.nombre, Queso1.variedad, Queso1.edad, Queso1.lleva_sal)
print("Queso 2: ", Queso2.nombre, Queso2.variedad, Queso2.edad, Queso2.lleva_sal)
print("Queso 3: ", Queso3.nombre, Queso3.variedad, Queso3.edad, Queso3.lleva_sal)