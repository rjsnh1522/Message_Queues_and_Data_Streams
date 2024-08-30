from rabbit.instagram_EDA.rabbit import get_rabbitmq_connection


def user_post_consumer(queue_name):
    connection, channel = get_rabbitmq_connection()

    # Consume messages
    def callback(ch, method, properties, body):
        print(f"Received in {queue_name}:", body)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(f'Waiting for messages in {queue_name}. To exit press CTRL+C')
    channel.start_consuming()