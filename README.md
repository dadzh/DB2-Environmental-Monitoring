# DB2-Environmental-Monitoring
Simulating IoT sensors to collect data on air quality, temperature, and humidity

This project shows how Docker connects many services together:
- MQTT
- MySQL
- MongoDB
- Neo4j
- Python publishers
- Python subscribers
- PHP

Air quality data -> MQTT -> MySQL
Temperature and humidity data -> MQTT -> MongoDB
Sensor room device data -> MQTT -> Neo4j

To start the project use following command in bash:
docker compose up --build

To open the dashboard of the project go to:
http://localhost:8080
