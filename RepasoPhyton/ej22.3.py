ciudades = {
    "Buenos Aires": "Argentina",
    "Madrid": "España",
    "París": "Francia",
    "Tokio": "Japón"
}

def describir_ciudad(ciudad, pais = "Argentina"):
        print(f"La ciudad {ciudad} esta en {pais}")

describir_ciudad("Buenos Aires")
describir_ciudad("Madrid", "España")
describir_ciudad("Paris", "Francia")
describir_ciudad("Tokio", "Japon")