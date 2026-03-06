import time

lista = ["pessi", "camellonaldo", "mile"]

print(lista[0], "Te invito a cenar asi me enseñas a jugar al futbol")
print(lista[1], "Te invito a cenar asi me enseñas a robar")
print(lista[2], "Te invito a cenar asi me cojes")
time.sleep(1)
print(lista[0], "no puede ir el pedazod e bot")

lista.remove("pessi")
lista.append("messi")

print(lista[2], "Te invito a cenar asi me enseñas a jugar al futbol")