print("-- Cursos --")
print("Matematica - Biologia - Lenguaje - Ciencias")

curso = input("Ingrese el curso deseado: ")

if curso in ("Matematica", "Biologia", "Lenguaje", "Ciencias"):
    print("Curso {0} seleccionado.".format(curso))
else:
    print("No existe ese curso...")
