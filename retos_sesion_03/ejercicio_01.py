class Atleta:
    def __init__(self, nombre, energia, fuerza):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza

    def entrenar(self):
        if self.energia > 0:
            self.fuerza += 2
            self.energia -= 1
            print(f"{self.nombre} entrenó. " f"Energía: {self.energia}, Fuerza: {self.fuerza}")
        else:
            print(f"{self.nombre} está demasiado cansado para entrenar.")

    def descansar(self):
        self.energia += 1
        print(f"{self.nombre} descansó. " f"Energía actual: {self.energia}")

    def comer(self, tipo_comida):
        if tipo_comida == 'hamburguesa':
            self.energia += 1
            print(f"{self.nombre} comió una hamburguesa. " f"Energía actual: {self.energia}")
        else:
            print(f"{self.nombre} comió {tipo_comida}. " f"La energía se mantiene igual.")

# Instanciando dos atletas
atleta_mariana = Atleta("Mariana", 10, 15)
atleta_lucas = Atleta("Lucas", 9, 20)

print("\nAcciones:")
atleta_mariana.entrenar()
atleta_lucas.entrenar()

atleta_mariana.descansar()
atleta_lucas.descansar()

atleta_mariana.comer("hamburguesa")
atleta_lucas.comer("apio")