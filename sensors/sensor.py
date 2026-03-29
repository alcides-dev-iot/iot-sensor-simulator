import random
import time

class Sensor:
    def __init__(self, name):
        self.name = name

    def read_temperature(self):
        return round(random.uniform(20, 30), 2)

    def read_humidity(self):
        return round(random.uniform(40, 60), 2)

    def generate_data(self):
        data = {
            "sensor": self.name,
            "temperature": self.read_temperature(),
            "humidity": self.read_humidity(),
            "timestamp": time.time()
        }
        return data