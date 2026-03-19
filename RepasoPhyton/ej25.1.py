def ingredientes_sandwich(*ingredientes):
    print("Tu sandwich contiene:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")


ingredientes_sandwich("queso", "tomate", "jamón")
ingredientes_sandwich("queso", "tomate")
