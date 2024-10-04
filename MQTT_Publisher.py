### EDGE
import json
import time
import requests

from paho.mqtt import client as mqtt_client

mqtt_ip = "localhost"  # "192.168.0.102"
mqtt_port = 1883
topic = "CSC8112"
# msg = "Hello!"


# Create a mqtt client object
client = mqtt_client.Client()


# Callback function for MQTT connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT OK!")
    else:
        print("Failed to connect, return code %d\n", rc)


# Connect to MQTT service
client.on_connect = on_connect
client.connect(mqtt_ip, mqtt_port)

# Publish message to MQTT
# Note: MQTT payload must be a string, bytearray, int, float or None
# Target URL
url = "https://newcastle.urbanobservatory.ac.uk/api/v1.1/sensors/PER_AIRMON_MONITOR1135100/data/json/?starttime=20230601&endtime=20230831"

# Request data from Urban Observatory Platform
resp = requests.get(url)

# Convert response(Json) to dictionary format
raw_data_dict = resp.json()
print(raw_data_dict)  # raw data
data = raw_data_dict["sensors"][0]["data"]["PM2.5"]  # filtered 2.5 data only
result = []
for index in data:
    timeStamp = index["Timestamp"]
    value = index["Value"]
    msg = f"Timestamp={timeStamp} Value={value}"
    result.append({'Timestamp': timeStamp, 'Value': value})
msg = json.dumps(result)
client.publish(topic, msg)  # sending data to task2
    #time.sleep(2)
