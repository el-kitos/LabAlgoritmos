libros = ["Don quijote"]

def libro_favorito(libro):
    if libro in libros:
        print("Es mi libro favorito")
    else:
        print("buen libro")
    
libro = input("Ingrese un libro: ").lower()

libro_favorito(libro)