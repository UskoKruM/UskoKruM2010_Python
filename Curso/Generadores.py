# Generadores: Permiten extraer valores de una función y almacenarlo
# (de uno en uno) en objetos iterables (que se pueden recorrer),
# sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM.

"""
def generaMultiplos7(limite):
    numero = 1
    listaNumeros = []

    while numero <= limite:
        listaNumeros.append(numero * 7)
        numero = numero + 1
    return listaNumeros  # Retorna toda la lista creada.

print(generaMultiplos7(10))
"""


def generadorMultiplos7(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
        numero = numero + 1


obtieneMultiplos7 = generadorMultiplos7(10)

"""
# print(obtieneMultiplos7)
for n in obtieneMultiplos7:
    print(n)
"""

# next(): Retorna el siguiente elemento de un objeto iterable:

print(next(obtieneMultiplos7))
print("Acá hay 300 líneas de código...")
print(next(obtieneMultiplos7))
print("Acá hay 1000 líneas de código...")
print(next(obtieneMultiplos7))

# Son más eficiente que las funciones tradicionales.
# Muy útiles con listas de valores infinitos.
# Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión).