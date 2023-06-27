""" la = list(range(5))
lb = list(range(-5,5))
lc = list(range(-5,5,2))

for l in la, lb, lc:
    print(l)



import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

l1 = letras[:8]
l2 = letras [8:16]
l3 = letras [16:]

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)

for a, b, c in zip(l1, l2, l3):
    print(a + b + c, end=' ') 

            """

import random

letras = list('abcdefghijklmnopqrstuvwxyz')
vocales = 'aeiou'

random.shuffle(letras)
print(''.join(letras))

for i, letra in enumerate(letras): # enumera TODAS las letras de la lista
    if letra in vocales: # itera por cada letra en la lista "letras" buscando la posicion de las vocales, tomando los datos de la STRING "vocales"
        print('{} en la posición {}'.format(letra, i)) 
        


abcde = sorted(letras)[:5]

# ejemplos de ENUMERATE

print("EJEMPLOS DE ENUMERATE")

print(list(enumerate(abcde)))

print(list(enumerate(abcde, 10)))

