import timeit


def my_function():
    for a in range(10000):
        a = a + 1

total_time = timeit.timeit(my_function, number=10000)

print(f"La función tomó {total_time} segundos.")
print(f"La función tomó {total_time * 1000} milisegundos.")
print(f"La función tomó {total_time * 1000000} microsegundos.")

"""
python -m timeit -s "from Curso.timeit_performance.tiempo_ejecucion import my_function" "my_function()"
python -m timeit -n 10 -s "from Curso.timeit_performance.tiempo_ejecucion import my_function" "my_function()"
python -m timeit -n 10 -r 12 -s "from Curso.timeit_performance.tiempo_ejecucion import my_function" "my_function()"
python -m timeit -n 10 -r 12 -u sec -s "from Curso.timeit_performance.tiempo_ejecucion import my_function" "my_function()"
python -m timeit -n 10 -r 12 -u sec -v -s "from Curso.timeit_performance.tiempo_ejecucion import my_function" "my_function()"
"""