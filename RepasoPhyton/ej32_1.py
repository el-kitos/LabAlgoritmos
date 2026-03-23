from pathlib import Path

path = Path("digitosDePi.txt")
content = path.read_text()

Cumple = input("Ingrese su fecha de cumpleaños: ")

if Cumple in content:
    print("Tu cumple esta en los digitos de pi")