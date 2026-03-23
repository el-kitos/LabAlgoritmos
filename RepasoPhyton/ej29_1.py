class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' es el mejor del mundo. Está en su peak. Su especialidad es la cocina {self.tipo_cocina}.")
        
class PuestoDeHelados(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = ["frutilla","chocolate","DDL"]
    
    def describir_PuestoDeHelados(self):
        print(f"El puesto de helados {self.nombre_restaurante} es el mejor. Su especialidad son los {self.tipo_cocina} y tiene los sabores {self.sabores}")
        

parrilla = Restaurante("Don Julio", "típica argentina")
pizzeria = Restaurante("Los Campeones", "pizzas porteñas")

Luccianos = PuestoDeHelados("Luccianos","Helados") 
Luccianos.describir_PuestoDeHelados()


parrilla.describir_restaurante()
pizzeria.describir_restaurante()



