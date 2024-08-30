from rabbit.instagram_EDA.rabbit import get_rabbitmq_connection


def user_auth_consumer():
    connection, channel = get_rabbitmq_connection()

    # Consume messages
    def callback(ch, method, properties, body):
        print("Received in user_auth_queue:", body)

    channel.basic_consume(queue='user_auth_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages in user_auth_queue. To exit press CTRL+C')
    channel.start_consuming()