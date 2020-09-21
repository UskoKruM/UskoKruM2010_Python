"""
Paquetes:
Directorios (carpetas) donde se almacenan módulos relacionados entre sí.

¿Para qué sirven?
Para organizar mejor el código y poder reutilizarlo mejor (modularización y reutilización).

¿Cómo se crea un paquete?
Crear una carpeta o directorio con un archivo dentro llamado __init__.py

Lo que hace __init__.py es "convertir" un directorio en un modulo (paquete)
que contiene otros módulos, y esto lo hace para poder importarlos.
"""

from Paquete1.funcionesCadena import contarLetras
from Paquete1.funcionesNumericas import *

print(multiplicar(5, 6))
print(contarLetras("UskoKruM2010"))
