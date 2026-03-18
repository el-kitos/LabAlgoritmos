print("Nos quedamos sin sandwiches de pastron")

pedidos_sandwiches = ["pastron" ,"jamon", "pastron" ,"aaaa", "salame", "pastron"]
sandwiches_terminados = []

while "pastron" in pedidos_sandwiches:
    pedidos_sandwiches.remove("pastron")

for sandwich in pedidos_sandwiches:
    print(f"Tu sandiwch de {sandwich}")
    sandwiches_terminados.append(sandwich)
    

print(f"Estos son los sandwiches terminados: {sandwiches_terminados}")