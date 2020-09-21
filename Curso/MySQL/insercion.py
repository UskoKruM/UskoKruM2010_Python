import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='condominio'
    )

    if conexion.is_connected():
        print("Conexión exitosa.")
        cursor = conexion.cursor()
        nombre = input("Ingrese nombre de usuario: ")
        # cursor.execute("INSERT INTO tipousuario (nombre) VALUES ('Vigilante')")
        sentencia = "INSERT INTO tipousuario (nombre) VALUES ('{0}')".format(nombre)
        cursor.execute(sentencia)
        conexion.commit()  # Confirmar la acción que estamos ejecutando.
        print("Registro insertado con éxito.")
except Error as ex:
    print("Error durante la conexión:", ex)
finally:
    if conexion.is_connected():
        conexion.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")
