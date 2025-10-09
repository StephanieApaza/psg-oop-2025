class Atleta:
    def __init__(self, nombre, energia, fuerza):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza

    def entrenar(self):
        if self.energia > 0:
            self.fuerza += 2
            self.energia -= 1
            print(f"{self.nombre} entrenó. Ahora tiene una energía: {self.energia} y fuerza: {self.fuerza}")
        else:
            print(f"{self.nombre} está demasiado cansado para entrenar.")

    def descansar(self):
        self.energia += 1
        print(f"{self.nombre} descansó. Recuperó más energia, ahora tiene una energía: {self.energia}")

    def comer(self, comida):
        if comida == 'hamburguesa':
            self.energia += 1
            print(f"{self.nombre} comió una hamburguesa. Recuperó energía, ahora tiene una energía: {self.energia}")
        else:
            print(f"{self.nombre} comió una comida distinta a hamburguesa. Su energía se mantiene igual.")

# Instanciando dos atletas
atleta1 = Atleta("Mariana", 10, 15)
atleta2 = Atleta("Lucas", 9, 20)

atleta1.entrenar()
atleta2.entrenar()
atleta1.descansar()
atleta2.descansar()
atleta1.comer('hamburguesa')
atleta2.comer('apio')