# Excepción: Error en tiempo de ejecución (durante la ejecución de un programa).

numero1 = 20
numero2 = 2

# print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))

try:
    resultado = numero1 / numero2
# except:
except ZeroDivisionError:
    print("No se puede dividir entre 0...")
finally:
    print("Yo siempre aparezco.")

print("Aquí termina mi programa.")
