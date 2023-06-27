"""
t = [(1, 2), (3, 4), (5, 6)]
for x, y in t:
    print(x + y, end=' ') 
                          # En este ejemplo estamos recorriendo una lista de  >              
                          # tuplas y las vamos asignando a dos variables >
                          # simultáneamente (x, e y) que luego utilizamos dentro >
                          # del "print" para ir sumándolas.
                          # Este proceso se llama desempaquetado en tuplas.


"""

keys = ['Nombre', 'Apellidos', 'Edad']
values = ['Pablo', 'Antón Gorgoroso', '41']

d = dict(zip(keys, values))

for k, v in d.items(): # Vemos que el método dict.items nos devuelve una >
                       # tupla (clave, valor) correspondiente a una entrada del >
                       # diccionario en cada iteración del for.
    print('{}: {}'.format(k, v))

