class Gato:
    especie = "felino"
    def __init__(self, color, genero, edad, castrado):
        self.color = color
        self.genero = genero
        self.edad = edad
        self.castrado = castrado

# Instanciar
pelusa = Gato("Negro", "hembra", 2, False)
miauricio = Gato("Naranja", "macho", 1, True)

# Mostrar atributos
print("Pelusa: ",pelusa.especie)
print(pelusa.color)
print(pelusa.genero)
print(pelusa.edad)
print(pelusa.castrado)

print("Miauricio: ",miauricio.especie)
print(miauricio.color)
print(miauricio.genero)
print(miauricio.edad)
print(miauricio.castrado)

print("Gato es: ", Gato.especie)