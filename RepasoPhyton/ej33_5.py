from pathlib import Path

try:
    path = Path("gatos.txt")
except FileNotFoundError:
    print("no se encontro el archivo")
else:
    pass
lista = ["rogi", "pedro", "nose"]
texto = "\n".join(lista)
path.write_text(texto)

path2 = Path("perros.txt")
lista2 = ["rodolfo", "alejandro", "alonso"]
texto2 = "\n".join(lista)
path2.write_text(texto)

