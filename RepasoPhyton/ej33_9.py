from pathlib import Path
import json

path = Path("hola.json")

if path.exists():
    contenido = path.read_text()
    numero = json.loads(contenido)
    print("Tu número favorito es:", numero)
else:
    numero = int(input("Ingrese su número favorito: "))
    contenido = json.dumps(numero)
    path.write_text(contenido)
    print("Guardamos tu número favorito.")