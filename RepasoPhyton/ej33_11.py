from pathlib import Path
import json

path = Path("usuario.json")


def obtener_nuevo_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    ciudad = input("Ingrese su ciudad: ")
    
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }
    
    contenido = json.dumps(usuario)
    path.write_text(contenido)
    
    return usuario


def saludar_usuario():
    if path.exists():
        try:
            contenido = path.read_text()
            usuario = json.loads(contenido)
        except:
            usuario = obtener_nuevo_usuario()
            print("\nEl archivo estaba vacío o dañado. Se guardaron nuevos datos.")
            return
        
        print("¿Tu nombre es", usuario["nombre"], "?")
        respuesta = input("(si/no): ")
        
        if respuesta == "si":
            print("\nEl programa recuerda esto sobre vos:")
            print("Nombre:", usuario["nombre"])
            print("Edad:", usuario["edad"])
            print("Ciudad:", usuario["ciudad"])
        else:
            usuario = obtener_nuevo_usuario()
            print("\nAhora el programa recuerda esto sobre vos:")
            print("Nombre:", usuario["nombre"])
            print("Edad:", usuario["edad"])
            print("Ciudad:", usuario["ciudad"])
    
    else:
        usuario = obtener_nuevo_usuario()
        print("\nEl programa ahora recuerda esto sobre vos:")
        print("Nombre:", usuario["nombre"])
        print("Edad:", usuario["edad"])
        print("Ciudad:", usuario["ciudad"])


saludar_usuario()