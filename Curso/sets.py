# Sets: son colecciones desordenadas de objetos únicos.

"""
canasta = {'manzana', 'platano', 'pera', 'manzana', 'naranja', 'pera'}
print(canasta)

numeros = {1, 3, 5, 8, 3, 4, 12, 1}
print(numeros)

# Tipo 1 de Sets: Set mutables
a = set('abracadabra')  # Mutables, se pueden añadir nuevos elementos
print(a)
a.add('g')
print(a)
a.add('a')
print(a)

# Tipo 2 de Sets: Set inmutables (no se pueden añadir nuevos elementos)
b = frozenset('perro')
print(b)
b.add('k')
print(b)
"""

# Intersecciones:
# miSet = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})
# miSet = {1, 2, 3, 4, 5} & {3, 4, 5, 6}

# Union
# miSet = {1, 2, 3, 4, 5}.union({3, 4, 5, 6})
# miSet = {1, 2, 3, 4, 5} | {3, 4, 5, 6}

# miSet = {1, 2, 3, 4}.difference({2, 3, 5})
# miSet = {1, 2, 3, 4} - {2, 3, 5}

# miSet = {1, 2, 3, 4}.symmetric_difference({2, 3, 5})

# miSet = {1, 2, 3, 4, 5}.issuperset({1, 2, 3})
miSet = {1, 2, 3, 4, 5}.issubset({1, 2, 3})
print(miSet)
