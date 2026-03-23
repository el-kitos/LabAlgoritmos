from pathlib import Path

path = Path("guestbook.txt")

lista = []

while True:
    opcion = input("Ingrese su nombre (o 'salir' para terminar): ")
    
    if opcion == "salir":
        break
    lista.append(opcion)
    
texto = "\n".join(lista)
path.write_text(texto)

