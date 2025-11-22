# Definición
class Destino:
    """Representa un destino turístico con nombre y costo en USD."""
    def __init__(self, nombre, costo):
        self.__nombre = nombre
        self.__costo = costo

    def __str__(self):
        return f"{self.__nombre} ➡ {self.__costo} USD"
    
class Catalogo:
    """Catálogo de destinos turísticos."""
    def __init__(self):
        self.__lista_destinos = []

    def __len__(self):
        return len(self.__lista_destinos)
    
    def __getitem__(self, indice):
        return self.__lista_destinos[indice]
    
    def __setitem__(self, indice, destino):
        if not isinstance(destino, Destino):
            raise TypeError("Solo se pueden agregar objetos de tipo Destino.")
        self.__lista_destinos[indice] = destino

    def __delitem__(self, indice):
        del self.__lista_destinos[indice]

    def __iter__(self):
        return iter(self.__lista_destinos)
    
    def agregar_destino(self, destino):
        if not isinstance(destino, Destino):
            raise TypeError("Solo se pueden agregar objetos de tipo Destino.")
        self.__lista_destinos.append(destino)
    
    def __str__(self):
        titulo = "🗺  Destinos🗺"
        destinos_formateados = [f"{indice_lista + 1}. {str(destino)}" for indice_lista, destino in enumerate(self.__lista_destinos)]
        listado = "\n".join(destinos_formateados)
        return f"{titulo}\n{listado}"
    
# Uso
# Crear destinos
destino_uno = Destino("La Paz", 120)
destino_dos = Destino("Uyuni", 350)
destino_tres = Destino("Santa Cruz", 200)
destino_cuatro = Destino("Copacabana", 90)

# Crear catálogo
catalogo = Catalogo()

catalogo.agregar_destino(destino_uno)
catalogo.agregar_destino(destino_dos)
catalogo.agregar_destino(destino_tres)
catalogo.agregar_destino(destino_cuatro)

print(catalogo)