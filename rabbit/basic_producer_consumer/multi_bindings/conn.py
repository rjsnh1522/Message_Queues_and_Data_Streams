import pika

def get_rabbitmq_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    return connection, channel
