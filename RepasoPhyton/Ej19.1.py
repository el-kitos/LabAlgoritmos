ingredientes = []
opcion = ""
while opcion != "salir":
    opcion = input("Ingrese ingredientes para la pizza('salir' para salir): ")
    if opcion != "salir":
        ingredientes.append(opcion)

print(ingredientes)