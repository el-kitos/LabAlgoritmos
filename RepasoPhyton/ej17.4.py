ciudades = {
    "Buenos Aires": {
        "pais": "Argentina",
        "poblacion": "3 millones",
        "dato": "Tiene el Obelisco como símbolo"
    },
    "Paris": {
        "pais": "Francia",
        "poblacion": "2 millones",
        "dato": "Es famosa por la Torre Eiffel"
    },
    "Tokio": {
        "pais": "Japón",
        "poblacion": "14 millones",
        "dato": "Es una de las ciudades más pobladas del mundo"
    }
}

for ciudad, info in ciudades.items():
    print(f"Ciudad: {ciudad}")
    print(f"Pais: {info['pais']}")
    print(f"Poblacion: {info['poblacion']}")
    print(f"Dato: {info['dato']}")
    print()