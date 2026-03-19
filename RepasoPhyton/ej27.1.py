class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
    
    def describir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' es el mejor del mundo. Está en su peak. Su especialidad es la cocina {self.tipo_cocina}.")

parrilla = Restaurante("Don Julio", "típica argentina")
pizzeria = Restaurante("Los Campeones", "pizzas porteñas")

parrilla.describir_restaurante()
pizzeria.describir_restaurante()