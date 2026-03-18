lugares_favoritos = {
    "Juan": ["Parque", "Cine"],
    "Alma": ["Playa"],
    "Marcos": ["Montaña", "Shopping", "Estadio"]
}

for persona, lugares in lugares_favoritos.items():
    print(persona, "tiene como lugares favoritos:")
    
    for lugar in lugares:
        print("-", lugar)
    
    print()