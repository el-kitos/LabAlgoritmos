import random

Loteria = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
ganadores = []

my_ticket = 5
i = 0
while True:
    ganador = random.choice(Loteria)
    ganadores.append(ganador)
    i+=1
    if ganador == 5:
        print(f"Me tomo {i} veces antes que salga mi numero")
        break

print(f"Los que tengan algun numero de estos: {ganadores} gano un premio 67676767")