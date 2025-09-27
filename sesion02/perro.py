class Perro:
    especie = "canino"
    tipo = "mamifero"
    habitat = "terrestre"
    def __init__(self, nombre, edad, genero, raza, vacunado, propietario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.raza = raza
        self.vacunado = vacunado
        self.propietario = propietario

# Instanciar
shagido = Perro("Shagido", 1, "Macho", "Labrador", True, "Mario")
jordan = Perro("Jordan", 2, "Macho", "Mestizo", True, "Lulú")

# Mostrar atributos
print("Shagido: ",shagido.especie, shagido.tipo, shagido.habitat)
print(shagido.nombre)
print(shagido.edad)
print(shagido.genero)
print(shagido.raza)
print(shagido.propietario)
print("Jordan: ",jordan.especie, jordan.tipo, jordan.habitat)
print(jordan.nombre)
print(jordan.edad)
print(jordan.genero)
print(jordan.raza)
print(jordan.propietario)

print("Perro es: ", Perro.tipo, "Especie: ", Perro.especie, "Habitat: ", Perro.habitat)