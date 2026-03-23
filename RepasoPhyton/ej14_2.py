usuarios = ["admin","juan", "pepe","malvasio"]

if not usuarios:
    print("Necesitamos usuarios")
else:
    for i in usuarios:
        if i != "admin":
            print(f"Hola {i} gracias por iniciar sesion")
        else:
            print("Hola admin te gustaria ver un informe")
