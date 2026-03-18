data = {}

cant_usuarios = 3

for i in range(cant_usuarios):
    nombre = input("Dime tu nombre: ")
    destino = input("Dime tu destino soñado: ")
    data[nombre] = destino

print("resultados de la encuesta")

for usuario, lugar in data.items():
    print(f"el {usuario} elijio el lugar {lugar}")
    print()