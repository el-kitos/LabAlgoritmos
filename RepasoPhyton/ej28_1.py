class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0
    
    def describir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' es el mejor del mundo. Su especialidad es la cocina {self.tipo_cocina}.")
        
    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad
        
    def incrementar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad



restaurante = Restaurante("Don Julio", "típica argentina")
print(restaurante.clientes_atendidos)


restaurante.clientes_atendidos = 10
print(restaurante.clientes_atendidos)

restaurante.establecer_clientes_atendidos(25)
print(restaurante.clientes_atendidos)

restaurante.incrementar_clientes_atendidos(5)
print(restaurante.clientes_atendidos)