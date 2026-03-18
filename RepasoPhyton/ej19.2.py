numeroClientes = int(input("Cuantos son?: "))
i = 1


while i <= numeroClientes:
    edad = int(input("Cuantos años tenes?: "))
    if edad < 3:
        print("Tu entrada es gratis")
    elif edad > 3 and edad < 12:
        print("Tu entrada sale 10$")
    else:
        print("Tu entrada cuesta 20$")
    i+=1
    
    if numeroClientes > i:
        break

    