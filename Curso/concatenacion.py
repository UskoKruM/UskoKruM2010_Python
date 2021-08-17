texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)

print("El saludo es: %s %s" % (texto1, texto2))

saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
print(saludoFinal)

saludoFinal2 = "Saludo: {y} {x}".format(x=texto2, y=texto1)
print(saludoFinal2)