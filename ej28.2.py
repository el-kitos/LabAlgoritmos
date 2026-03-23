class Usuario:
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.intentos_login = 0

    def describir_usuario(self):
        print(f"El usario se llama {self.nombre} {self.apellido}, su email es {self.email} y tiene {self.edad} años ")
    
    def saludar(self):
        print(f"hola {self.nombre}")
    
    def incrementar_intentos_login(self):
        self.intentos_login+=1
    
    def reiniciar_intentos_login(self):
        self.intentos_login = 0
    

juanjo = Usuario("Juanjo", "Alfonso","juanjoalfonso@gmail", "8")

juanjo.describir_usuario()
juanjo.saludar()

Marcos = Usuario("Marcos","Bertoglio", "Marcos@gmail.com", "16")
Marcos.describir_usuario()
Marcos.saludar()

Marcos.incrementar_intentos_login()
Marcos.incrementar_intentos_login()
Marcos.incrementar_intentos_login()
Marcos.incrementar_intentos_login()

print(Marcos.intentos_login)

Marcos.reiniciar_intentos_login()

print(Marcos.intentos_login)