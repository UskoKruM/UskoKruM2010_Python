# Polimorfismo (poli => muchas / morfos: formas)

class Estudiante():

    def describir(self):
        print("Soy un buen estudiante.")


class Docente():

    def describir(self):
        print("Me dedico a enseñar cursos.")


class Trabajador():

    def describir(self):
        print("Trabajo dentro de una gran empresa.")


def describirPersona(persona):
    persona.describir()


doc1 = Trabajador()
describirPersona(doc1)
