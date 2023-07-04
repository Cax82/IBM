number = 3

def codigo_3(number):
    a = 0

    for j in range(1, number+1):
        for k in range(1, number+1):
            a += a + (k*j)

    return a

codigo_3(number)