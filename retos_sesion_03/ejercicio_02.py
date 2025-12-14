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
        self.productividad_individual = 0

    # Método de instancia
    def cocinar(self, receta):
        if receta not in Cocinero.recetas_definidas:
            print(f"La receta {receta} no esta en el sistema.")
            return
        
        ingredientes_necesarios = Cocinero.recetas_definidas[receta]
        faltan_ingredientes = [ingrediente for ingrediente in ingredientes_necesarios if ingrediente not in self.ingredientes]

        if not faltan_ingredientes:
            print(f"{self.nombre} cocinó {receta}")
            self.productividad_individual += 1 
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
cocinero_amalia = Cocinero("Amalia", ['harina', 'agua', 'sal', 'tomate', 'queso'])
cocinero_leonardo = Cocinero("Leonardo", ['harina', 'agua', 'sal', "chocolate"])
cocinero_elena = Cocinero("Elena",['harina'])
print("--------------------------------------------------------------------")
Cocinero.verificar_receta("pizza")
Cocinero.verificar_receta("galleta")
Cocinero.verificar_receta("queque")
print("--------------------------------------------------------------------")
cocinero_amalia.cocinar("pizza")
cocinero_leonardo.cocinar("galleta")
cocinero_elena.cocinar("pan")
print("--------------------------------------------------------------------")
print(f"{cocinero_amalia.nombre}: {cocinero_amalia.productividad_individual}")
print(f"{cocinero_leonardo.nombre}: {cocinero_leonardo.productividad_individual}")
print(f"{cocinero_elena.nombre}: {cocinero_elena.productividad_individual}")

# Productividad total
Cocinero.mostrar_productividad_total()