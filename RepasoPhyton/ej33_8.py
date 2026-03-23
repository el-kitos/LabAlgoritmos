from pathlib import Path
import json

numero = int(input("Ingrese su numero favorito: "))

path = Path("hola.json")
contenido = json.dumps(numero)
path.write_text(contenido)

