mensajes = ["Hola que onda","Chau","Como estas"]

def mostrar_nesnajes(mensajes):
    for i in mensajes:
        print(i)
def enviar_mensajes(mensajes):
    mensajes_enviados = mensajes.copy()
    print(f"{mensajes[0]}")
    print(f"{mensajes[1]}")
    print(f"{mensajes[2]}")
    mensajes.clear()

mostrar_nesnajes(mensajes)  