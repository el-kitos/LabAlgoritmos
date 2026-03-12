frutas_favoritas = ['manzana', 'naranja', 'uva',]
frutas_favoritas2 = []

for i in range(len(frutas_favoritas)):
    frutaFavorita = input('¿Cuál es tu fruta favorita? ')
    frutas_favoritas2.append(frutaFavorita)
    
for i in frutas_favoritas2:
    if i in frutas_favoritas:
        print("Te gustan las frutas como a mi!")

print(frutas_favoritas2)