# Listas: Son estructuras de datos que nos permiten almacenar distintos valores
# (equivalentes a los arrays en otros lenguajes de programación)

# Son estructuras dinámicas, pueden MUTAR.

lista1 = ["Oscar", 25, 98.3, True, "Flavio", 56.3]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])

print(lista1[0:3])
print(lista1[:2])
print(lista1[3:])

lista1.append("UskoKruM2010")
print(lista1)

lista1.insert(4, "Perú")
print(lista1)

lista1.extend(["Alejandro", 110, False])
print(lista1)

print(lista1.index("Flavio"))

lista1.remove(56.3)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["Chiclayo", "Irma"]
lista3 = lista1 + lista2
print(lista3)

print(lista2 * 4)

print("UskoKruM2010" in lista1)
