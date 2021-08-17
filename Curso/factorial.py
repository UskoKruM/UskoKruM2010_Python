# Factorial: Es el producto de todos los números positivos enteros comprendidos entre 1 y un número.

# Factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
# Factorial de 4: 1 * 2 * 3 * 4 = 24

numero = int(input("Ingrese un número: "))

factorial = 1
for n in range(1, (numero + 1)):
    factorial = factorial * n

print("El factorial de {0} es: {1}".format(numero, factorial))
