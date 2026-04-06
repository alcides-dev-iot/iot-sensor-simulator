import time
import json
import paho.mqtt.client as mqtt
from sensors.sensor import Sensor

# Configuración MQTT
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensor/data"


def main():
    # Crear sensor
    sensor = Sensor("ESP32-Simulator")

    # Crear cliente MQTT
    client = mqtt.Client()

    # Conectar al broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    print("Connected to MQTT broker")

    while True:
        # Generar datos del sensor
        data = sensor.generate_data()

        # Convertir a JSON
        payload = json.dumps(data)

        # Publicar en MQTT
        client.publish(MQTT_TOPIC, payload)

        print(f"Sent: {payload}")

        time.sleep(2)


if __name__ == "__main__":
    main()
