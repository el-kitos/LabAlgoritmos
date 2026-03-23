class Usuario:
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad

    def describir_usuario(self):
        print(f"El usario se llama {self.nombre} {self.apellido}, su email es {self.email} y tiene {self.edad} años ")
    
    def saludar(self):
        print(f"hola {self.nombre}")
    

juanjo = Usuario("Juanjo", "Alfonso","juanjoalfonso@gmail", "8")

juanjo.describir_usuario()
juanjo.saludar()