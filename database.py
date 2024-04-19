import mysql.connector
from mysql.connector import Error

# Configura la conexión a la base de datos
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='raspberry_data',
        user='gerard',
        password='gerard'
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado a MySQL Server version ", db_Info)
        cursor = connection.cursor()

        # Ejemplo de inserción de datos
        sensor_id = 1
        temperature_value = 25.5
        humidity_calue = 35

        # Query para insertar datos en la tabla 'temperature'
        insert_query = "INSERT INTO temperature_data (sensor_id, temperature) VALUES (%s, %s)"
        data = (sensor_id, temperature_value)

        # Ejecutar la consulta
        cursor.execute(insert_query, data)

        # Confirmar la transacción
        connection.commit()
        print("Datos insertados correctamente en la tabla 'temperature'")

except Error as e:
    print("Error al conectar a MySQL:", e)

finally:
    # Cerrar la conexión si está abierta
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a MySQL cerrada")
