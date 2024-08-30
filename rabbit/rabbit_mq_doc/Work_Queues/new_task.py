import sys

import pika

from conn import get_rabbitmq_connection

connection, channel = get_rabbitmq_connection()

channel.queue_declare(queue='task_queue', durable=True)
# durable true is to make sure queue and messages dont get lost if RQ
# stops working and we need to restart this

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
    )
)
# persistent delivery is to make sure messages are durable
# and dont get lost when anything goes wrong before message is processed
# so we keep them in disk

print(f" [x] Sent {message}")
connection.close()