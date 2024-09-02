import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='multi_binding', exchange_type='direct')

queue = channel.queue_declare(queue='orange')

queue_name = queue.method.queue

channel.queue_bind(exchange='multi_binding',
                   queue=queue_name,
                   routing_key='orange')


def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(f'receiving in only from orange: {payload}')
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=queue_name, on_message_callback=callback)

print("Waiting for orange messages. to exit press cmd C")

channel.start_consuming()
