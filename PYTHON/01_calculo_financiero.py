capital = int(input("Introduzca el capital que desea invertir: "))
tipo = float(input("Introduzca el tipo de interés: "))
periodo = int(input("Indique los años: "))


def vf(capital, tipo, periodo):
    for i in range(periodo):
        print("Año", i, ":", capital * (1 + tipo /100)** (i + 1))
    return


def va(capital, tipo, periodo):
    for i in range(periodo):
        print("Año", -i, ":", capital / (1 + tipo /100)** (i + 1))
    return

print("Valor Futuro")
vf(capital, tipo, periodo)
print("Valor Actual")
va(capital, tipo, periodo)