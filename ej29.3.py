class Usuario:
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad

    def describir_usuario(self):
        print(f"El usuario se llama {self.nombre} {self.apellido}, su email es {self.email} y tiene {self.edad} años")
    
    def saludar(self):
        print(f"hola {self.nombre}")


class Privilegios:
    def __init__(self):
        self.privilegios = [
            "puede agregar publicaciones",
            "puede eliminar publicaciones",
            "puede bloquear usuarios"
        ]
    
    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for privilegio in self.privilegios:
            print("-", privilegio)


class Administrador(Usuario):
    def __init__(self, nombre, apellido, email, edad):
        super().__init__(nombre, apellido, email, edad)
        self.privilegios = Privilegios()



admin = Administrador("Juanjo", "Alfonso", "juanjoalfonso@gmail", 8)

admin.describir_usuario()
admin.saludar()

admin.privilegios.mostrar_privilegios()