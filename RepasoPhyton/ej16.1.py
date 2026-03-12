glosario = {
    "variable": "espacio donde se guarda un dato en un programa",
    "lista": "estructura que permite guardar varios elementos en orden",
    "diccionario": "estructura que guarda datos en pares de clave y valor",
    "funcion": "bloque de codigo que realiza una tarea especifica",
    "bucle": "estructura que repite un bloque de codigo varias veces"
}

for palabra in glosario.keys():
    print(f"{palabra} : {glosario[palabra]}")

glosario["condicional"] =  "estructura que ejecuta codigo solo si se cumple una condicion"
glosario["string"] = "tipo de dato que representa texto"
glosario["entero"] = "tipo de dato que representa numeros sin decimales"
glosario["booleano"] = "tipo de dato que solo puede tener dos valores: verdadero o falso"
glosario["parametro"] = "dato que se pasa a una funcion para que lo use"

print("/nGlosario actualizado")

for palabra in glosario.keys():
    print(f"{palabra} : {glosario[palabra]}")