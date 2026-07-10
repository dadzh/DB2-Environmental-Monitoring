import json
import time
import mysql.connector
import paho.mqtt.client as mqtt

BROKER = "mqtt"
PORT = 1883
TOPIC = "iot/air_quality"

def connect_mysql():
    while True:
        try:
            return mysql.connector.connect(
                host="mysql",
                user="root",
                password="root",
                database="iot_project"
            )
        except:
            print("Waiting for MySQL...")
            time.sleep(3)

db = connect_mysql()
cursor = db.cursor()

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    sql = '''
    INSERT INTO air_quality_readings
    (sensor_id, room_name, air_quality, status)
    VALUES (%s, %s, %s, %s)
    '''

    values = (
        data["sensor_id"],
        data["room_name"],
        data["air_quality"],
        data["status"]
    )

    cursor.execute(sql, values)
    db.commit()

    print("Saved to MySQL:", data)

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(TOPIC)

print("SQL subscriber is listening...")
client.loop_forever()
