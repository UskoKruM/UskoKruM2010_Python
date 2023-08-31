def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar mi_funcion")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar mi_funcion")
        return resultado
    return wrapper


@mi_decorador
def mi_funcion():
    print("Esta es mi función")


mi_funcion()
