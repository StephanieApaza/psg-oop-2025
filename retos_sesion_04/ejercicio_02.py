class Celula:
    def __init__(self, adn, tipo_celula, energia):
        self.__adn = adn
        self.tipo_celula = tipo_celula
        self.__energia = energia

    @property
    def energia(self):
        return self.__energia
    
    @property
    def adn(self):
        return self.__adn
    
    # Mostrar datos de la célula    
    def mostrar_datos(self):
        print(f"ADN: {self.__adn}, Tipo: {self.tipo_celula}, Energía: {self.__energia}")
    
    # Método para dividir la célula
    def dividir_celula(self, energia_consumida):
        if 0 < energia_consumida <= self.__energia:
            self.__energia -= energia_consumida
            print(f"La celula gastó {energia_consumida} de energía al dividirse. La energía actual es: {self.__energia}.")
        else:
            print(f"No hay suficiente energía para dividirse. La energía actual es: {self.__energia}")

    # Método para comer de la célula
    def comer_celula(self, energia_adquirida):
        if energia_adquirida > 0:
            self.__energia += energia_adquirida
            print(f"La celula consumió {energia_adquirida} de energía. La energía actual es: {self.__energia}")
        else:
            print(f"El alimento no propociona energía. La energía actual es: {self.__energia}")

# Implementando la clase
celula_vegetal = Celula("ACTB134", "Vegetal", 10)
celula_animal = Celula("CHTS567", "Animal", 9)
print("--------------------------------------------------------------------")
celula_vegetal.mostrar_datos()
celula_animal.mostrar_datos()
print("--------------------------------------------------------------------")
celula_vegetal.comer_celula(2)
celula_vegetal.dividir_celula(3)
celula_vegetal.mostrar_datos()
print("--------------------------------------------------------------------")
celula_animal.comer_celula(7)
celula_animal.dividir_celula(5)
celula_animal .mostrar_datos()