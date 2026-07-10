import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "mqtt"
PORT = 1883
TOPIC = "iot/air_quality"

def get_status(air_quality):
    if air_quality > 100:
        return "bad"
    elif air_quality > 50:
        return "moderate"
    else:
        return "good"

client = mqtt.Client()
client.connect(BROKER, PORT)

counter = 1
rooms = ["SBA2_2", "EDIFICIO_B", "MENSA"]

while True:
    air_quality = random.randint(10, 150)

    data = {
        "sensor_id": f"AIR_{counter}",
        "room_name": random.choice(rooms),
        "air_quality": air_quality,
        "status": get_status(air_quality)
    }

    client.publish(TOPIC, json.dumps(data))
    print("Published SQL data:", data)

    counter += 1
    time.sleep(5)
