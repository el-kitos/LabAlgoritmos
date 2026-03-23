import time
#lista = ["maradona","camellonaldo","pele", "mile","centu" ]
lista = ["pessi", "camellonaldo", "zahir"]

print(lista[0], "Te invito a cenar asi me enseñas a jugar al futbol")
print(lista[1], "Te invito a cenar asi me enseñas a robar")
print(lista[2], "Te invito a cenar asi te gano en el fifa")
time.sleep(1)
print(lista[0], "no puede ir el pedazod e bot")

lista.remove("pessi")
lista.append("messi")

print(lista[2], "Te invito a cenar asi me enseñas a jugar al futbol")
time.sleep(1)

print("Chicos consegui una mesa mas grande")
time.sleep(1)
lista.insert(0, "maradona")
print(lista[0], "Te invito a cenar asi me enseñas a jugar al futbol")
time.sleep(1)
lista.insert(2, "pele")
print(lista[2], "Te invito a cenar asi me enseñas a jugar al futbol")
lista.append("centu")
print(lista[4], "Te invito a cenar asi me enseñas a jugar al futbol")

print("los invitados son: ", lista)

print("Chicos, la mesa se va a romper, solo pueden venir dos personas")
time.sleep(1)
print("Lamento mucho que no puedas venir ", lista.pop(0))
time.sleep(1)
print("Lamento mucho que no puedas venir ", lista.pop(0))
time.sleep(1)
print("Lamento mucho que no puedas venir ", lista.pop(0))
time.sleep(1)
print("Lamento mucho que no puedas venir ", lista.pop(0))
time.sleep(1)
print("Los invitados que quedan son: ", lista)
del lista[0]
del lista[0]
print("Los invitados que quedan son: ", lista, "nadie jajaja")

print("estoy invitando a cenar a", len(lista), "personas")
