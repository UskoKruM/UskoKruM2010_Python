# Función: Es un conjunto de instrucciones que realizan un proceso.
# Su principal ventaja es que nos ayudan a evitar código repetido.

def saludar():
    print("García")
    print("Oscar")
    print("UskoKruM2010")
    return "Hola"

print(saludar())

def evaluarSueldoMinimo(sueldo):
    if sueldo >= 850:
        print("Cumples con el sueldo")
    else:
        print("Ganas menos que el sueldo mínimo")

evaluarSueldoMinimo(100)
