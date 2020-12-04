# Funciones de orden superior (programación funcional).

# Verificar que los elementos de una lista cumplan una determinada condición, devolviendo
# un objeto iterable (iterador) con los elementos que cumplieron esa condición.

edades = [12, 11, 24, 36, 8, 6, 10, 41, 32, 58, 14, 50, 7]


def mayorEdad(edad):
    return edad >= 18


# print(filter(mayorEdad, edades))
edadesMayoresEdad = list(filter(mayorEdad, edades))


# print(edadesMayoresEdad)

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{0} tiene {1} años.".format(self.nombre, self.edad)


personas = [
    Persona("Alberto", 32),
    Persona("Ana", 16),
    Persona("Andy", 27),
    Persona("Jesús", 25),
    Persona("Cecilia", 19),
    Persona("Laura", 30),
]

personasMayoresEdad = list(filter(lambda per: per.edad >= 18, personas))
# print(personasMayoresEdad)

for per in personasMayoresEdad:
    print(per)