cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue # En el siguiente ejemplo vemos como al encontrar la letra P >
                 # se llama al continue, lo que hace que se salte el print(). >
                 # Es por ello por lo que no vemos la letra P impresa en pantalla.
    print(letra)