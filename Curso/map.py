# Map: Aplica una función a cada elemento de una lista iterable, devolviendo otra lista.

def elevarCuadrado(num):
    # return num * num
    return pow(num, 2)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))  # 1 al 10
print(numeros)

# numerosElevados = map(elevarCuadrado, numeros)
numerosElevados = list(map(elevarCuadrado, numeros))
print(numerosElevados)