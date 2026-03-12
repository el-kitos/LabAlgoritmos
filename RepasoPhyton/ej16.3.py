lenguajes_favoritos = {'Juan': 'python',
                        'Sara': 'c', 
                        'Eduardo': 'rust', 
                        'Agustina': 'c#'}

personas = ["Juan", "Hola", "Pedro", "Agustina"]

for persona in lenguajes_favoritos.keys():
    if persona in personas:
        print(f"Gracias por responder la encuesta {persona}")
    else:
        print(f"Te invito a participar{persona}")