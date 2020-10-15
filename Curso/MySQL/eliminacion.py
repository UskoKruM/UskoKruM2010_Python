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
        cursor.execute("DELETE FROM tipousuario WHERE codigo = 8")
        conexion.commit()  # Confirmar la acción que estamos ejecutando.
        print("Registro eliminado con éxito.")
except Error as ex:
    print("Error durante la conexión:", ex)
finally:
    if conexion.is_connected():
        conexion.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")
