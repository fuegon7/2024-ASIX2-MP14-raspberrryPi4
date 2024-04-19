import adafruit_dht
import board
import RPi.GPIO as GPIO
import time

# Definir el número de pin GPIO al que está conectado el LED
led_pin = 18

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Definir el tipo de sensor y el número del pin GPIO al que está conectado
sensor = adafruit_dht.DHT22(board.D4)  # Ajusta este valor al número de pin GPIO que estás utilizando

# Variable para controlar el estado del LED y el mensaje
temperatura_alta_detectada = False

try:
    while True:
        # Intentar leer la temperatura y la humedad desde el sensor
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity

            if temperature is not None and humidity is not None:
                print("Temperatura={0:0.1f}C  Humedad={1:0.1f}%".format(temperature, humidity))
                
                # Verificar si la temperatura supera los 29 grados Celsius
                if temperature > 29.0 and not temperatura_alta_detectada:
                    # Encender el LED
                    GPIO.output(led_pin, GPIO.HIGH)
                    print("¡Alerta! Temperatura alta. Encendiendo LED.")
                    
                    # Establecer la bandera para indicar que se ha detectado una temperatura alta
                    temperatura_alta_detectada = True
                
                # Si la temperatura vuelve a ser menor o igual a 29 grados Celsius, apagar el LED
                if temperature <= 29.0 and temperatura_alta_detectada:
                    GPIO.output(led_pin, GPIO.LOW)
                    print("Temperatura normal. Apagando LED.")
                    temperatura_alta_detectada = False
            
            else:
                print("Error al leer datos del sensor. Inténtalo de nuevo.")

        except RuntimeError as error:
            print(error.args[0])  # Mostrar el mensaje de error
            continue  # Continuar con el siguiente intento de lectura

        # Esperar un segundo antes de la próxima lectura
        time.sleep(1)

except KeyboardInterrupt:
    print("\nLectura de temperatura detenida por el usuario.")
finally:
    sensor.exit()  # Liberar recursos del sensor
    GPIO.cleanup()  # Limpiar los pines GPIO al finalizar el script
