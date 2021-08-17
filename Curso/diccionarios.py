# Diccionarios: Son estructuras de datos que nos permiten almacenar distintos
# valores.

# Es que los datos se almacenan asociados a una clave única, tenemos una relación
# clave:valor

# Los elementos almacenados están en desorden, el orden es indiferente a la forma
# de almacenamiento.

miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
print(miDiccionario["Perú"])
print(miDiccionario)

miDiccionario["Venezuela"] = "Caracas"
print(miDiccionario)

miDiccionario["España"] = "Barcelona"
print(miDiccionario)

del miDiccionario["España"]
print(miDiccionario)

dic2 = {"García": "Oscar", 25: True, "Sueldo": 150.80}
print(dic2[25])

llaves = ("España", "Francia", "Inglaterra")
dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
print(dicPaises)

datosPersonales = {"Ape": "García", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
print(datosPersonales)
print(datosPersonales["Anios"])

print(datosPersonales.get('Apel', "Oscar"))

print(datosPersonales.keys())
valores = tuple(datosPersonales.values())
print(valores)
