pizzas = ["muzzarella","napolitana", "fugazzeta"]
listaAmigo = pizzas.copy()
listaAmigo.append("jamon y morrones")
pizzas.append("calabresa")

for i in pizzas:
    if i == "muzzarella":
        print("Me gusta mucho la pizza de muzzarella")
    elif i == "napolitana":
        print("Me gusta la pizza napolitana")
    elif i == "calabresa":
        print("Me gusta la pizza de calabresa")
    else:
        print("Me gusta la pizza de fugazzeta")

print("mis pizas favoritas son:")
for i in pizzas:
    print(i)

print("Las pizzas favoritas de mi amigo son:")
for i in listaAmigo:
    print(i)
