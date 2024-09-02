import uuid

import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='multi_binding', exchange_type='direct')

order = {
    "msg": "from producer_1 for black and green"
}

channel.basic_publish(exchange='multi_binding',
                      routing_key="black",
                      body=json.dumps(order))

print(" Message sent on black")


connection.close()

