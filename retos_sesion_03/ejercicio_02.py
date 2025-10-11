class Cocinero:
    recetas_definidas = {
            'pan': ['harina', 'agua'],
            'pizza': ['harina', 'agua', 'sal', 'tomate', 'queso'],
            'galleta': ['harina', 'agua', 'sal', 'chocolate']}
    
    # Métrica agregada de productividad
    productividad_total = 0
    
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.productividad = 0

    # Método de instancia
    def cocinar(self, receta):
        if receta not in Cocinero.recetas_definidas:
            print(f"La receta {receta} no esta en el sistema.")
            return
        
        ingredientes_necesarios = Cocinero.recetas_definidas[receta]
        faltan_ingredientes = [ingrediente for ingrediente in ingredientes_necesarios if ingrediente not in self.ingredientes]

        if not faltan_ingredientes:
            print(f"{self.nombre} cocinó {receta}")
            self.productividad += 1 
            Cocinero.productividad_total += 1

        else:
            print(f"{self.nombre} no puede preparar {receta}. Le falta: {faltan_ingredientes}")
        
    # Método de clase    
    @classmethod
    def mostrar_productividad_total(cls):
        print(f"La productividad total de todos los cocineros es: {cls.productividad_total}")

    # Método estático para verificar si una receta esta disponible
    @staticmethod
    def verificar_receta(receta):
        if receta in Cocinero.recetas_definidas:
            print(f"La receta {receta} es válida.")
        else:
            print(f"La receta {receta} no es válida.")

# Instanciando tres Cocineros y probando sus métodos
cocinero1 = Cocinero("Amalia", ['harina', 'agua', 'sal', 'tomate', 'queso'])
cocinero2 = Cocinero("Leonardo", ['harina', 'agua', 'sal', "chocolate"])
cocinero3 = Cocinero("Elena",['harina'])
print("--------------------------------------------------------------------")
Cocinero.verificar_receta("pizza")
Cocinero.verificar_receta("galleta")
Cocinero.verificar_receta("queque")
print("--------------------------------------------------------------------")
cocinero1.cocinar("pizza")
cocinero2.cocinar("galleta")
cocinero3.cocinar("pan")
print("--------------------------------------------------------------------")
print(f"{cocinero1.nombre}: {cocinero1.productividad}")
print(f"{cocinero2.nombre}: {cocinero2.productividad}")
print(f"{cocinero3.nombre}: {cocinero3.productividad}")

# Productividad total
Cocinero.mostrar_productividad_total()