class Animal:
    origen = "feral"
    def __init__(self, especie, tipo, lugar):
        self.especie = especie
        self.tipo = tipo
        self.lugar = lugar

print("Animales registrados:")
animal_uno = Animal("Mamífero", "Carnívoro", "Sudáfrica")
animal_dos = Animal("Mamífero", "Hervíboro", "Bolivia")
animal_tres = Animal("Reptil", "Carnívoro", "Australia")
animal_cuatro = Animal("Ave", "Carnívoro", "Estados Unidos")

print("Animal 1: ", animal_uno.origen, animal_uno.especie, animal_uno.tipo, animal_uno.lugar)
print("Animal 2: ", animal_dos.origen, animal_dos.especie, animal_dos.tipo, animal_dos.lugar)
print("Animal 3: ", animal_tres.origen, animal_tres.especie, animal_tres.tipo, animal_tres.lugar)
print("Animal 4: ", animal_cuatro.origen, animal_cuatro.especie, animal_cuatro.tipo, animal_cuatro.lugar)