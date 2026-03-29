# IoT Sensor Simulator with Real-Time Dashboard

This project simulates a real IoT system where a virtual sensor generates environmental data (temperature and humidity) and sends it to a real-time dashboard using MQTT.


## Features

- Simulated IoT device (like ESP32)
- Real-time data generation (temperature & humidity)
- MQTT communication protocol
- Live dashboard visualization using Node-RED
- Modular and scalable architecture


## Architecture

Sensor Simulator (Python) → MQTT Broker → Node-RED → Dashboard UI


## Technologies Used

- Python
- MQTT (Mosquitto)
- Node-RED
- JSON data handling


## Dashboard Preview

![alt text](image.png)


## ▶How to Run

### 1. Start MQTT Broker
Mosquitto runs automatically on most systems. If needed:

    mosquitto

### 2. Activate Python Environment

    source venv/bin/activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Run the sensor simulator

    python main.py

### 5. Start Node-RED

    node-red

### 6. Open Dashboard
Go to:

    http://localhost:1880/ui



## Use Cases

- IoT system prototyping
- Real-time monitoring dashboards
- Sensor data simulation
- MQTT-based communication systems


## Future Improvements

- Cloud deployment (AWS / Azure)
- Data storage (database integration)
- AI-based anomaly detection
- Multi-device simulation

## Author

Alcides Castro

---

### Freelance Focus

I build IoT systems with real-time monitoring using MQTT, Python, and Node-RED dashboards.

Available for freelance work and IoT-related projects.