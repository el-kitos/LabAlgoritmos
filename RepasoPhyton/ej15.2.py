persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 20,
    "ciudad": "Buenos Aires"
}

print("Nombre:", persona["nombre"])
print("Apellido:", persona["apellido"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])

numerosFavs = {
    "Juan" : 7,
    "Alma" : 67,
    "Marcos" : 6,
    "Facu" : 7,
    "Nick" : 67
}
for nombre in numerosFavs.keys():
    print(f"Numero Favorito de {nombre} : {numerosFavs[nombre]}")