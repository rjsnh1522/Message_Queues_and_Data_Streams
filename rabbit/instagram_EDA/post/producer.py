from rabbit.instagram_EDA.rabbit import get_rabbitmq_connection


def user_post_producer(action, content):
    connection, channel = get_rabbitmq_connection()

    # Publish a message
    message = {"post_id": "456", "user_id": "123", "action": action, "content": content}
    channel.basic_publish(exchange='user_post_exchange', routing_key='', body=str(message))

    connection.close()
