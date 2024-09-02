import uuid

import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='multi_binding', exchange_type='direct')

order = {
    "msg": "Message for orange only consumer_1"
}

channel.basic_publish(exchange='multi_binding',
                      routing_key="orange",
                      body=json.dumps(order))

print(" Message sent on orange")


connection.close()

