import json
import time
from pymongo import MongoClient
import paho.mqtt.client as mqtt

BROKER = "mqtt"
PORT = 1883
TOPIC = "iot/climate"

def connect_mongo():
    while True:
        try:
            client = MongoClient("mongodb://mongodb:27017/")
            client.admin.command("ping")
            return client
        except:
            print("Waiting for MongoDB...")
            time.sleep(3)

mongo_client = connect_mongo()
db = mongo_client["iot_project"]
collection = db["climate_readings"]

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    collection.insert_one(data)
    print("Saved to MongoDB:", data)

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(TOPIC)

print("MongoDB subscriber is listening...")
client.loop_forever()
