class Curso():
    """
    nombre = "Matemática"
    creditos = 5
    profesion = "Ingeniería Civil"
    """

    # Estado inicial del objeto:
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"  # Propiedad encapsulada.

    def mostrarDatos(self):
        dat = "Nombre: {0} / Créditos: {1} / Modo de impartición: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asignado.")
        else:
            print("No es necesario asignar un docente...")

    def __verificarDocente(self):
        # print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False

    # toString()
    def __str__(self):
        texto = "Nombre: {0} - Créditos: {1}"
        return texto.format(self.nombre, self.creditos)


curso1 = Curso("Matemática", 5, "Ingeniería Civil")
print(curso1)
curso1.mostrarDatos()

# curso2 = Curso("Lenguaje", 4, "Ingeniería Industrial")
# print(curso2.nombre)
