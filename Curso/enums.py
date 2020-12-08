from enum import Enum


class Color(Enum):
    rojo = '#ff0000'
    verde = '#008000'
    azul = '#0000ff'


# print(Color.verde.value)
# print(Color('#0000ff'))
# print(Color['rojo'].value)

lista = list([c for c in Color])
print(lista)
print(len(lista))

for a in lista:
    print(a.value)
