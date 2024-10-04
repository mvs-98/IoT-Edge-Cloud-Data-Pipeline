import pika
import json
if __name__ == '__main__':
    rabbitmq_ip = "localhost"
    rabbitmq_port = 5672
    # Queue name
    rabbitmq_queque = "CSC8112"
    msg = "Hello!"
    # Connect to RabbitMQ service
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_ip, port=rabbitmq_port))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue=rabbitmq_queque)

    # Produce message
    channel.basic_publish(exchange='',
                      routing_key=rabbitmq_queque,
                      body=json.dumps(msg))
    connection.close()