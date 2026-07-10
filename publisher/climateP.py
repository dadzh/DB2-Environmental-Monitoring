import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "mqtt"
PORT = 1883
TOPIC = "iot/climate"

client = mqtt.Client()
client.connect(BROKER, PORT)

counter = 1
rooms = ["SBA2_2", "EDIFICIO_B", "MENSA"]

while True:
    data = {
        "sensor_id": f"CLIMATE_{counter}",
        "room_name": random.choice(rooms),
        "temperature": round(random.uniform(18, 35), 2),
        "humidity": round(random.uniform(30, 85), 2)
    }

    client.publish(TOPIC, json.dumps(data))
    print("Published MongoDB data:", data)

    counter += 1
    time.sleep(3)
