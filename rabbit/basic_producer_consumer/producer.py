import uuid

import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='order', exchange_type='direct')

order = {
    "id": str(uuid.uuid4()),
    "user_email": "test@email.com",
    "producer": "leather jacket",
    "quantity": 1,
}

channel.basic_publish(exchange='order', routing_key="order.notify", body=json.dumps(order))

print(" Message sent on order.notify")


channel.basic_publish(exchange='order', routing_key="order.report", body=json.dumps(order))

print(" Message sent on order.report")

connection.close()

