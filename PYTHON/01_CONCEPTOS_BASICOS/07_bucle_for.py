lista = ['Me', 'gusta', 'Python!']  # en una Lista

for s in lista:
    print(s, end=' ')


for c in "Me gusta Python!":   # en una String
    print(c, end=' ')


keys =['Nombre', 'Apellidos', 'Edad'] # en diccionarios
values = ['Pablo', 'Antón', '41']

d = dict(zip(keys, values))

for k in d:
    info = '{}: {}'.format(k, d[k])

    print(info)
