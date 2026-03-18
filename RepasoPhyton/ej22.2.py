texto = input("Ingrese el texto de la camiseta: ")
tamaño = ""
def hacer_camiseta(texto, tamaño = "XL"):
    print(f"El tamaño dicho es {tamaño} y el texto es {texto}")
    
    if tamaño == "XL":
        print("Me encanta Phyton")

hacer_camiseta(texto)
