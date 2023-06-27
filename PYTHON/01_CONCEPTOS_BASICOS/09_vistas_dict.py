""" Tened en cuenta que a partir de Python 3.5, el
método dict.items devuelve una vista de los
elementos del diccionario, es decir, no devuelve los
objeto en sí hasta que no los recorramos o los
convirtamos explícitamente en listas. Otros métodos
tienen el mismo comportamiento son dict.keys y
dict.values, que devuelven vistas de las claves y los
valores respectivamente.  """

keys = ['Nombre', 'Apellidos', 'Edad']
values = ['Pablo', 'Antón Gorgoroso', '41']

d = dict(zip(keys, values))

for k in d.keys():
    print(k, end=' ')

for v in d.values():
    print(v, end=" ")



