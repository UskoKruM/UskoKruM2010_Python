texto = "bienveNIdos al canal de uskokrum2010"

print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title()) # Convierte una cadena a un formato de título.
print(texto.find("al")) # Posición donde encuentra la cadena o porción.
print(texto.count("e")) # Cantidad de ocurrencias de una letra o porción.

textoFinal = texto.replace("e", "3")
print(textoFinal)

valor = texto.isnumeric() # Arroja true o false dependiendo si es un número.
print(valor)

cadenaSeparada = texto.split(" ")
print(cadenaSeparada)