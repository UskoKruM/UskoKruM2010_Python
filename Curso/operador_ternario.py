"""
String sexo;
sexo = (10 > 20) ? "Masculino" : "Femenino";
"""

sexos = ("Hombre", "Mujer")

posicion = True
sexo = sexos[posicion] # Mujer
print(sexo)
sexo = sexos[not posicion] # Hombre
print(sexo)