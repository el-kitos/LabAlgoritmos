usuariosActuales = ["marki32", "zahir32", "nicki32", "facu32","juanjo32"]

usuariosNuevos = ["marki32", "zahir32", "nicki79", "facu79","juanjo79"] 

for i in usuariosNuevos:
    i = i.lower()
    if i in usuariosActuales:
        print("este usuario ya fue usado")
    if i not in usuariosActuales:
        print("usuario disponible")