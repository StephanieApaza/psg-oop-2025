# Definiendo la clase
class Vizcacha:
    def __init__(self):
        self.estado = 'Feliz'
        self.escondido = False
    
    def comer(self, comida):
        if comida == '🥕':
            print(f"Vizcacha esta comiendo {comida}")
        else:
            print(f"Vizcacha no come {comida}")

    def excavar(self): # Método de instancia
        print("Vizcacha está excavando un agujero")
        self.escondido = True
        self.estado = "asustada"
        print(f"Vizcacha esta {self.estado}")

    def silvar(self): # Método de instancia
        print("iiih iiih")
        self.estado = "feliz"
        print(f"Vizcacha esta {self.estado}")

# Instanciando un objeto
vizcacha = Vizcacha()
vizcacha.comer("🥕")
vizcacha.comer("🍔")
vizcacha.excavar()
vizcacha.silvar()