persona1 = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 20,
    "ciudad": "Buenos Aires"
}

persona2 = {
    "nombre": "Alma",
    "apellido": "Gomez",
    "edad": 19,
    "ciudad": "Cordoba"
}

persona3 = {
    "nombre": "Marcos",
    "apellido": "Lopez",
    "edad": 21,
    "ciudad": "Rosario"
}

gente = [persona1, persona2, persona3]

for persona in gente:
    print("Nombre:", persona["nombre"])
    print("Apellido:", persona["apellido"])
    print("Edad:", persona["edad"])
    print("Ciudad:", persona["ciudad"])
    print()