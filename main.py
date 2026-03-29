import time
from sensors.sensor import Sensor

def main():
    sensor = Sensor("ESP32-Simulator")

    while True:
        data = sensor.generate_data()
        print(data)
        time.sleep(2)

if __name__ == "__main__":
    main()