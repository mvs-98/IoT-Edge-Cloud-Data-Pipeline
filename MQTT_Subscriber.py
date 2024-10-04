### EDGE
from datetime import datetime
import json
import pika

from paho.mqtt import client as mqtt_client

if __name__ == '__main__':
    mqtt_ip = "localhost"
    mqtt_port = 1883
    topic = "CSC8112"
    ct = []
    # Create a mqtt client object
    client = mqtt_client.Client()


    # Callbacsk function for MQTT connection
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT OK!")
        else:
            print("Failed to connect, return code %d\n", rc)


    # Connect to MQTT service
    client.on_connect = on_connect
    client.connect(mqtt_ip, mqtt_port)


    # Callback function will be triggered
    def on_message(client, userdata, msg):
        ct = json.loads(msg.payload)
        outliersData = []
        for d in ct:
            # print(d)
            value1 = d['Value']
            # print(value1)
            if value1 >= 50:
                outliersData.append(d)
        print("outliers :", outliersData)
        current_date = None
        daily_count = 0
        daily_total = 0
        daily_average = []
        for entry in ct:
            timestamp = entry['Timestamp']
            value = entry['Value']
            date = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
            if date != current_date:
                if current_date is not None:
                    daily_average.append({'Date': current_date, 'Average_PM2.5': daily_total / daily_count})
                    current_date = date
                    daily_total = value
                    daily_count = 1
                else:
                    current_date = date

            else:
                daily_total += value
                daily_count += 1
        print("New format ", daily_average)
        ##################RabbitMQ producer########################
        rabbitmq_ip = "localhost"
        rabbitmq_port = 5672
        # Queue name
        rabbitmq_queque = "CSC8112"
        # Connect to RabbitMQ service
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_ip, port=rabbitmq_port))
        channel = connection.channel()
        # Declare a queue
        channel.queue_declare(queue=rabbitmq_queque)

        # Produce message
        channel.basic_publish(exchange='',
                          routing_key=rabbitmq_queque,
                          body=json.dumps(daily_average))
        connection.close()
        ############################################
    # Subscribe MQTT topic
    client.subscribe(topic)
    client.on_message = on_message

    # Start a thread to monitor message from publisher
    client.loop_forever()
    # client.loop()