# Cuando indicamos un * adelante del parámetros de una función,
# estamos indicado que se va a recibir un número indeterminado
# de parámetros. Además, esos parámetros se recibirán en forma de tupla.

"""
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng
"""

def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng

lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
