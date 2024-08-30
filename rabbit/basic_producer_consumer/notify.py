import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

queue = channel.queue_declare(queue='order_notify')

queue_name = queue.method.queue

channel.queue_bind(exchange='order', queue=queue_name, routing_key='order.notify')

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(f'Notified for the payload: {payload}')
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=queue_name, on_message_callback=callback)

print("Waiting for notify messages. to exit press cmd C")

channel.start_consuming()
