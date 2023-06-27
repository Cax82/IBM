"""for num in [1, 2, 3, 4, 5, 6]:
    print(num ** 2, end=' ')

for num in [12, 38, 99, 1]:
    print(num / 2, end=' ')

for letra in 'Python':
    print(letra.upper(), end=' ')

""" 
zen = """\
    Bello es mejor que feo.
    Explícito es mejor que implícito.
    Simple es mejor que complejo.
    Complejo es mejor que complicado."""


f = open('short_zen.txt', "w") 

f.writelines(zen) # Escribe el fichero

f.close()

f = open('short_zen.txt', 'r')
f.__next__()





