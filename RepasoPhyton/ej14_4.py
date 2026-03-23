lista = list(range(1,10))

for i in lista:
    if i == 1:
        print(f"{i}ero")
    elif i == 2:
        print(f"{i}do")
    elif i == 3:
        print(f"{i}ero")
    elif i >= 4 and i <= 6:
        print(f"{i}to")
    elif i == 7:
        print(f"{i}mo")
    elif i == 8:
        print(f"{i}vo")
    else:
        print(f"{i}no")