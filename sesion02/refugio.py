class Mascota:
    origen = "abandonado"
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie


print ("Mascotas encontradas...")
perro = Mascota("Perro 001", "perro")
gato = Mascota("Gato 002", "gato")

print("Mascota 1: ",perro.origen, perro.nombre, perro.especie)
print("Mascota 2: ",gato.origen, gato.nombre, gato.especie)

print("Rescatando mascotas...")
Mascota.origen = "rescatado"
perro.nombre = "Milaneso"
gato.nombre = "Kitty"

print("Mascotas rescatadas...")
print("Mascota 1: ",perro.origen, perro.nombre, perro.especie)
print("Mascota 2: ",gato.origen, gato.nombre, gato.especie)