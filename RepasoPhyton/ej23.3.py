def hacer_album(artista, titulo, canciones=None):
    album = {
        "artista": artista,
        "titulo": titulo
    }

    if canciones is not None:
        album["canciones"] = canciones

    return album


while True:
    print("\nIngresá los datos del álbum (escribí 'salir' para terminar)")

    artista = input("Artista: ")
    if artista.lower() == "salir":
        break

    titulo = input("Título del álbum: ")
    if titulo.lower() == "salir":
        break

    cant = input("Cantidad de canciones (opcional): ")

    if cant == "":
        album = hacer_album(artista, titulo)
    else:
        album = hacer_album(artista, titulo, int(cant))

    print("Álbum creado:", album)