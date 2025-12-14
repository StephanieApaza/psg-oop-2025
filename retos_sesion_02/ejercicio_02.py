class Vino:
    def __init__(self, nombre, tipo, cepa, anio_produccion):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio_produccion = anio_produccion

print("Vinos registrados:")
vino_uno = Vino("Antinori Tignanello", "Tinto", "Sangiovenese con Cabernet", 2018)
vino_dos = Vino("Chateau", "Tinto", "Cabernet Sauvignon", 2015)
vino_tres = Vino("Cloudy Bay Sauvignon Blanc", "Blanco", "Sauvignon Blanc", 2021)
vino_cuatro = Vino("Moet & Chandon Imperial Brut", "Espumoso", "Pinot Noir y Meunier", 2010)

print("Vino 1: ", vino_uno.nombre, vino_uno.tipo, vino_uno.cepa, vino_uno.anio_produccion)
print("Vino 2: ", vino_dos.nombre, vino_dos.tipo, vino_dos.cepa, vino_dos.anio_produccion)
print("Vino 3: ", vino_tres.nombre, vino_tres.tipo, vino_tres.cepa, vino_tres.anio_produccion)
print("Vino 4: ", vino_cuatro.nombre, vino_cuatro.tipo, vino_cuatro.cepa, vino_cuatro.anio_produccion)

class Queso:
    def __init__(self, nombre, variedad, edad, lleva_sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad   # En meses
        self.lleva_sal = lleva_sal

print("\nQuesos registrados: ")
queso_uno = Queso("Roquefort", "Azul - de leche de vaca", 2, True)
queso_dos = Queso("Parmigiano-Reggiano", "Duro - de leche de vaca", 1, False)
queso_tres = Queso("Manchego", "Semicurado - de leche de oveja manchega", 3, True)

print("Queso 1: ", queso_uno.nombre, queso_uno.variedad, queso_uno.edad, queso_uno.lleva_sal)
print("Queso 2: ", queso_dos.nombre, queso_dos.variedad, queso_dos.edad, queso_dos.lleva_sal)
print("Queso 3: ", queso_tres.nombre, queso_tres.variedad, queso_tres.edad, queso_tres.lleva_sal)