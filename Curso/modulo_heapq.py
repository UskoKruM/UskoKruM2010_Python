import heapq

numeros = [1, 4, 2, 100, -15, 20, 760, 50, 32, 150, 8]

resultado = heapq.nlargest(3, numeros)
print(type(resultado))

resultado2 = heapq.nsmallest(2, numeros)
print(resultado2)

# https://docs.python.org/es/3/library/heapq.html