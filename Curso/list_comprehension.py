import math

# numeros = [1, 4, 9, 16, 25]

# La lista interna es asignada a la variable cuando todos los elementos han
# sido procesados:
# raices = [int(math.sqrt(x)) for x in numeros]

"""
raices = []
for n in numeros:
    raices.append(int(math.sqrt(n)))
"""

# print(raices)

# v = [x if (x > 10) else '*' for x in numeros]

# print(v)

# l = [c.upper() for c in 'UskoKruM2010']
# print(l)

a = [l if l in 'aeiou' else '*' for l in 'murcielago']
print(a)
