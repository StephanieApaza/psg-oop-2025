# Definición
class Departamento:
    def __init__(self, numero, inquilinos):
        self.numero = numero
        self.inquilinos = inquilinos

class Oficina:
    def __init__(self, numero, telefono):
        self.numero = numero
        self.telefono = telefono

class Piso:
    def __init__(self, numero):
        self.numero = numero
        self.departamentos = []
        self.oficinas = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def agregar_oficina(self, oficina):
        self.oficinas.append(oficina)

class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pisos = []

    def agregar_piso(self, piso):
        self.pisos.append(piso)

    def mostrar_info(self):
        print(f"Edificio: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        for piso in self.pisos:
            print(f"Piso: {piso.numero}")
            if piso.departamentos:
                print("Departamentos:")
                for departamento in piso.departamentos:
                    print(f"Número: {departamento.numero}, Inquilinos: {','.join(departamento.inquilinos) if departamento.inquilinos else 'Sin inquilinos'}")
            else:
                print("No hay departamentos")

            if piso.oficinas:
                print("Oficinas")
                for oficina in piso.oficinas:
                    print(f"Número: {oficina.numero}, Teléfono: {oficina.telefono}")
            else:
                print("No hay oficinas")

# Uso
edificio = Edificio("Dos Torres", "Av. Arce 3256")

piso1 = Piso(1)
piso2 = Piso(2)
piso3 = Piso(3)

# Agregando departamento y oficinas al piso 1
piso1.agregar_departamento(Departamento(101, ["Jaime Illanes", "Ana Suarez"]))
piso1.agregar_oficina(Oficina("2A", 25738248))

# Agregar departamentos y oficinas al piso 2
piso2.agregar_departamento(Departamento(201, ["Lisa Gutierrez"]))
piso2.agregar_oficina(Oficina("2A", 27834821))

# Agregar departamentos y oficinas al piso 3
piso3.agregar_departamento(Departamento(301, []))
piso3.agregar_oficina(Oficina("3A", 26734011))
piso3.agregar_oficina(Oficina("3B", 27493471))

# Agregar pisos
edificio.agregar_piso(piso1)
edificio.agregar_piso(piso2)
edificio.agregar_piso(piso3)

edificio.mostrar_info()