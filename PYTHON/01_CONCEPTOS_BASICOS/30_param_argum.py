la = [1, 2, 3, 4, 5]
lb = list('abcde')
lc = list('ABCDE')
zlist = list(zip(la, lb, lc)) # zip soporta cualquier número de argumentos posicionales
a, b, c = zip(*zlist) # El * en zip desempaqueta lista de tuplas
print(la, lb, lc, sep = '\n')
print(la, lb) # Seperador por defecto es espacio
