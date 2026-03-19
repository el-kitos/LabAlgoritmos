class Perro:
    """Un intento simple de modelar un perro."""
    def __init__(self, nombre, edad):
        """Inicializa los atributos nombre y edad."""
        self.nombre = nombre
        self.edad = edad
    def sentarse(self):
        """Simula que el perro se siente cuando se lo ordenás."""
        print(f"{self.nombre} ahora se sentó.")
    def acostarse(self):
        """Simula que el perro se acuesta panza arriba cuando se lo ordenás."""
        print(f"{self.nombre} se tiró panza arriba!")

mi_perro = Perro("Pimpón", 3)
tu_perro = Perro("Tintín", 5)
print(f"Mi perro se llama {mi_perro.nombre}.")
print(f"Tu perro se llama {tu_perro.nombre}.")
mi_perro.sentarse()
tu_perro.acostarse()

