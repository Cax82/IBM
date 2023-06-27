"""
Lista = list()
Set = ()

l = int(input("Introduzca el tamaño de la Lista: "))
s = int(input("Introduzca el tamaño del Set: "))

print("Introduzca los elementos de la Lista: ")
for i in range(0, 1):
    list.append(int(input()))

print("Introduzca los elementos del Set: ")
for i in range(0, 5):
    Set.add(int(input()))

print(Lista)
print(Set)

List = list()
Set = set()
l = int(input("Introduzca el tamaño de la lista: "))
s = int(input("Introduzca el tamaño del Set: "))
print("Introduzca los elementos de la lista:")
for i in range(0, 1):
    list.append(int(input()))
print("Introduzca los elementos del Set: ")
for i in range(0, 5):
    Set.add(int(input()))
print(list)
print(set)


"""

# Uso de los métodos map() y list() / set(). Se puede ingresar varios datos en el mismo Input.

List = list(map(int, input("Introduzca los elementos de la lista:").split()))
Set = set(map(int, input("Introduzca los elementos del Set: ").split()))
print(List)
print(Set)