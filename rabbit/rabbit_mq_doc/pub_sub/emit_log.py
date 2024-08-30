import sys

from conn import get_rabbitmq_connection

conn, channel = get_rabbitmq_connection()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or 'info: hello world!'
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(f" [x] Sent {message}")
conn.close()