def hacer_album(artista, titulo, canciones=None):
    album = {
        "artista": artista,
        "titulo": titulo
    }

    if canciones is not None:
        album["canciones"] = canciones

    return album


# Crear tres álbumes
album1 = hacer_album("Bad Bunny", "Un Verano Sin Ti")
album2 = hacer_album("Duki", "Desde el Fin del Mundo")
album3 = hacer_album("Taylor Swift", "1989")

# Imprimir resultados
print(album1)
print(album2)
print(album3)

# Nueva llamada con cantidad de canciones
album4 = hacer_album("Travis Scott", "Astroworld", 17)
print(album4)