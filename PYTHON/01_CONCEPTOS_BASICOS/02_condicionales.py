
# Los ejemplos de condicionales, pasados a una Función.
def calificacion():
    nota= int(input("Introduce tu nota: "))
    if nota<5:
        print("Suspenso")
    elif nota<7:
        print("Aprobado")
    elif nota<9:
        print("Notable")
    else:
        print("Sobresaliente")

calificacion()