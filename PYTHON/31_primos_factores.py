def descomp_num(numero):
    factores = []
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            factores.append(divisor)
            numero = numero / divisor
        else:
            divisor += 1

    return  factores

numero = int(input("Indica un número: "))
factores = descomp_num(numero)
print(f"Factores de {numero}: {factores}")
