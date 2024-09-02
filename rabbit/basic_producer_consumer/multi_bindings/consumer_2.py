import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='multi_binding', exchange_type='direct')

queue = channel.queue_declare(queue='black')

queue_name = queue.method.queue


channel.queue_bind(exchange='multi_binding',
                   queue=queue_name,
                   routing_key='black')

queue2 = channel.queue_declare(queue='green')
queue2_name = queue2.method.queue
channel.queue_bind(exchange='multi_binding',
                   queue=queue2_name,
                   routing_key='green')


def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(f'receiving in black and green: {payload}')
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=queue_name, on_message_callback=callback)
channel.basic_consume(queue=queue2_name, on_message_callback=callback)

print("Waiting for notify messages. to exit press cmd C")

channel.start_consuming()
