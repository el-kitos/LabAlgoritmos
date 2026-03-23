import random

Loteria = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
ganadores = []

for i in range(4):
    ganador = random.choice(Loteria)
    ganadores.append(ganador)

print(f"Los que tengan algun numero de estos: {ganadores} gano un premio 67676767")
