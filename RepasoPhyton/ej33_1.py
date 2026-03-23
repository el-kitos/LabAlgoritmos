from pathlib import Path

nombre = input("Escriba su nombre: ")

path = Path("guest.txt")

path.write_text(nombre)