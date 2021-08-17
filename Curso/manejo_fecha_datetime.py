import datetime

# from datetime import datetime

fechaActual = datetime.datetime.now()
# print(fechaActual)

# fecha = datetime.datetime(2020, 11, 5)
# fecha = datetime.datetime(2020, 11, 5, 10, 35, 21)
# print(fecha)

# fechaActual2 = datetime.datetime.strftime(fechaActual, '%d/%m/%Y %H:%M:%S')
# print(fechaActual2)

# fechaActual3 = datetime.datetime.strftime(fechaActual, '%b %d %Y %H:%M:%S')
# print(fechaActual3)

# https://strftime.org/

# fechaTexto = 'Dec 06 2020 12:56:11'
# fechaActual4 = datetime.datetime.strptime(fechaTexto, '%b %d %Y %H:%M:%S')
# print(fechaActual4)

# dia = datetime.datetime.strftime(fechaActual, '%d')
# dia = int(datetime.datetime.strftime(fechaActual, '%d'))
# print(dia)

# horaActual = datetime.datetime.strftime(fechaActual, '%H:%M:%S')
# print(horaActual)

"""
fechaPasada = datetime.datetime(2020, 10, 23)
diferencia = fechaActual - fechaPasada
print(diferencia)
print(diferencia.days)
print(diferencia.total_seconds())
"""

"""
dia_delta = datetime.timedelta(days=-5)
fechaInicial = datetime.date.today()
print(fechaInicial)
fechaFutura = fechaInicial + dia_delta
print(fechaFutura)
"""

fecha = datetime.datetime.now().isoformat()
print(fecha)
