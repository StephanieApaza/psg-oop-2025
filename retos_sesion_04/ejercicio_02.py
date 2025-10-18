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
    def dividir_celula(self, division):
        if division > 0 and division <= self.__energia:
            self.__energia -= division
            print(f"La celula gastó {division} de energía al dividirse. La energía actual es: {self.__energia}.")
        else:
            print(f"No hay suficiente energía para dividirse. La energía actual es: {self.__energia}")

    # Método para comer de la célula
    def comer_celula(self, alimento):
        if alimento > 0:
            self.__energia += alimento
            print(f"La celula consumió {alimento} de energía. La energía actual es: {self.__energia}")
        else:
            print(f"El alimento no propociona energía. La energía actual es: {self.__energia}")

# Implementando la clase
celula1 = Celula("ACTB134", "Vegetal", 10)
celula2 = Celula("CHTS567", "Animal", 9)
print("--------------------------------------------------------------------")
celula1.mostrar_datos()
celula2.mostrar_datos()
print("--------------------------------------------------------------------")
celula1.comer_celula(2)
celula1.dividir_celula(3)
celula1.mostrar_datos()
print("--------------------------------------------------------------------")
celula2.comer_celula(7)
celula2.dividir_celula(5)
celula2.mostrar_datos()


