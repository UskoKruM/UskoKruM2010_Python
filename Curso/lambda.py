# Son funciones anónimas que sirven para abreviar o resumir una función normal,
# para convertirla en una expresión más simple.

"""
def sumar(n1, n2):
    return n1 + n2

print(sumar(12,15))
"""

# Toda función lambda se puede convertir a una función normal, no viceversa.

sumar1 = lambda n1, n2: n1 + n2

print(sumar1(45, 14))
miSuma = sumar1(80, 15)
print(miSuma)

elevarCuadrado = lambda numero: numero * numero

print(elevarCuadrado(5))
