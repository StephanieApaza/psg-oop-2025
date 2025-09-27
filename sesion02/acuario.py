class Pez:
    origen = "cautiverio"
    def __init__(self, especie, peso, agua):
        self.especie = especie
        self.peso = peso
        self.agua = agua

print ("Peces registrados...")
pez_uno = Pez("Pez angel", 0.4, "agua dulce")
pez_dos = Pez("Pez payaso", 0.9, "agua salada")

print("Pez 1: ",pez_uno.origen, pez_uno.especie, pez_uno.peso, pez_uno.agua)
print("Pez 2: ",pez_dos.origen, pez_dos.especie, pez_dos.peso, pez_dos.agua)

print("Liberando peces...")
pez_uno.peso = 0.6
pez_dos.peso = 1
Pez.origen = "Liberados"

print("Peces liberados...")
print("Pez 1: ",pez_uno.origen, pez_uno.especie, pez_uno.peso, pez_uno.agua)
print("Pez 2: ",pez_dos.origen, pez_dos.especie, pez_dos.peso, pez_dos.agua)