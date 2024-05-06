import mysql.connector
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Configurar el backend de matplotlib para visualización no interactiva
import matplotlib.pyplot as plt

connection = None  # Inicializar connection fuera del bloque try

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

        # Consulta SQL para recuperar datos de la tabla temperature_data
        query = "SELECT temperature_celsius FROM temperature_data"

        # Leer datos desde MySQL y cargarlos en un DataFrame de pandas
        df = pd.read_sql(query, connection)

        # Calcular estadísticas básicas usando pandas y numpy
        average_temperature = df['temperature_celsius'].mean()
        std_dev_temperature = df['temperature_celsius'].std()
        min_temperature = df['temperature_celsius'].min()
        max_temperature = df['temperature_celsius'].max()

        # Imprimir las estadísticas calculadas
        print("Estadísticas de Temperatura:")
        print(f"Promedio: {average_temperature:.2f} grados Celsius")
        print(f"Desviación Estándar: {std_dev_temperature:.2f} grados Celsius")
        print(f"Mínimo: {min_temperature:.2f} grados Celsius")
        print(f"Máximo: {max_temperature:.2f} grados Celsius")

        # Crear un gráfico de barras para visualizar las estadísticas
        plt.figure(figsize=(8, 6))
        plt.bar(['Promedio', 'Desviación Estándar', 'Mínimo', 'Máximo'],
                [average_temperature, std_dev_temperature, min_temperature, max_temperature],
                color='skyblue')
        plt.title('Estadísticas de Temperatura')
        plt.ylabel('Temperatura (grados Celsius)')

        # Guardar el gráfico como imagen
        plt.savefig('estadisticas_temperatura.png')
        print("Gráfico guardado como 'estadisticas_temperatura.png'")

except mysql.connector.Error as e:
    print("Error al conectar a MySQL:", e)

finally:
    # Cerrar la conexión a la base de datos si está definida
    if connection and connection.is_connected():
        connection.close()
        print("Conexión a MySQL cerrada")
