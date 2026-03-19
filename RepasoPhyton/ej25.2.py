def construir_perfil(nombre, apellido, **info_usuario):
    """Construye un diccionario con todo lo que sabemos sobre un usuario."""
    info_usuario['nombre'] = nombre
    info_usuario['apellido'] = apellido
    return info_usuario
perfil_usuario = construir_perfil('Marcos', 'Bertoglio', ubicacion='Buenos Aires',campo='Nose', Colegio = 'hOLA')
print(perfil_usuario)
