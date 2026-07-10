import json
import time
import requests
import paho.mqtt.client as mqtt

BROKER = "mqtt"
PORT = 1883
TOPIC = "iot/room_relation"

NEO4J_URL = "http://neo4j:7474/db/neo4j/tx/commit"
AUTH = ("neo4j", "password")

def wait_for_neo4j():
    while True:
        try:
            response = requests.post(
                NEO4J_URL,
                auth=AUTH,
                json={"statements": [{"statement": "RETURN 1"}]}
            )
            if response.status_code == 200:
                return
        except:
            pass

        print("Waiting for Neo4j...")
        time.sleep(3)

wait_for_neo4j()

def save_to_neo4j(data):
    cypher = '''
    MERGE (s:Sensor {id: $sensor_id})
    MERGE (r:Room {name: $room_name})
    MERGE (d:Device {name: $device})
    MERGE (s)-[:PLACED_IN]->(r)
    MERGE (r)-[:HAS_DEVICE]->(d)
    '''

    body = {
        "statements": [
            {
                "statement": cypher,
                "parameters": data
            }
        ]
    }

    requests.post(NEO4J_URL, auth=AUTH, json=body)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    save_to_neo4j(data)
    print("Saved to Neo4j:", data)

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(TOPIC)

print("Neo4j subscriber is listening...")
client.loop_forever()
