import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "mqtt"
PORT = 1883
TOPIC = "iot/room_relation"

client = mqtt.Client()
client.connect(BROKER, PORT)

counter = 1
rooms = ["SBA_2", "EDIFICIO_B", "MENSA"]
devices = ["Air Purifier", "Air Conditioner", "Heater"]

while True:
    data = {
        "sensor_id": f"SENSOR_{counter}",
        "room_name": random.choice(rooms),
        "device": random.choice(devices)
    }

    client.publish(TOPIC, json.dumps(data))
    print("Published Neo4j data:", data)

    counter += 1
    time.sleep(5)
