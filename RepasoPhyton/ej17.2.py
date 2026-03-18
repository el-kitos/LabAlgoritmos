mascota1 = {
    "nombre": "Firulais",
    "tipo": "Perro",
    "edad": 5,
    "duenio": "Juan"
}

mascota2 = {
    "nombre": "Michi",
    "tipo": "Gato",
    "edad": 3,
    "duenio": "Alma"
}

mascota3 = {
    "nombre": "Lola",
    "tipo": "Conejo",
    "edad": 2,
    "duenio": "Marcos"
}

mascotas = [mascota1, mascota2, mascota3]

for mascota in mascotas:
    print("Nombre:", mascota["nombre"])
    print("Tipo:", mascota["tipo"])
    print("Edad:", mascota["edad"])
    print("Dueño:", mascota["duenio"])
    print()