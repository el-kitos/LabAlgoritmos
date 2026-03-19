def hacer_auto(fabricante,modelo, **auto):
    auto["fabricante"] = "Alguien"
    auto["modelo"] = "corolla"
    return auto

hola = hacer_auto("Alguien","corolla", color = "azul", puertas = 4)

print(hola)