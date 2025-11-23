# Definición
class Destino:
    """Representa un destino turístico con nombre y costo en USD."""
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

    def __str__(self):
        return f"{self.nombre} ➡  {self.costo} USD"
    
class Catalogo:
    """Catálogo de destinos turísticos."""
    def __init__(self):
        self.lista_destinos = []

    def __str__(self):
        titulo = "🗺  Destinos🗺"
        destinos_formateados = [f"{indice_lista + 1}. {str(destino)}" for indice_lista, destino in enumerate(self.lista_destinos)]
        listado_destinos = "\n".join(destinos_formateados)
        return f"{titulo}\n{listado_destinos}"

    def __len__(self):
        return len(self.lista_destinos)
    
    def __getitem__(self, indice):
        return self.lista_destinos[indice]
    
    def __setitem__(self, indice, destino):
        self.lista_destinos[indice] = destino

    def __delitem__(self, indice):
        del self.lista_destinos[indice]

    def __iter__(self):
        return iter(self.lista_destinos)
    
# Uso
catalogo = Catalogo()
catalogo.lista_destinos.append(Destino("La Paz", 120))
catalogo.lista_destinos.append(Destino("Uyuni", 350))
catalogo.lista_destinos.append(Destino("Santa Cruz", 200))
catalogo.lista_destinos.append(Destino("Copacabana", 90))
print(catalogo)

# Cuantos destinos tiene el catálogo
longitud = len(catalogo)
print(f"Número de destinos: {longitud}")

# Acceder a los destinos por su indice
destino_uno = catalogo[0]
print(destino_uno)

# Agregar nuevos destinos 
catalogo[3] = Destino("Rurrenabaque", 400)
print(catalogo)

# Iterar sobre los destinos
for destino in catalogo:
    print(destino)

# Eliminar un destino del catálogo
del catalogo[2]
print(catalogo)