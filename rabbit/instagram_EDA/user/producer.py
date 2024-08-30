from rabbit.instagram_EDA.rabbit import get_rabbitmq_connection


def user_auth_producer(action):
    connection, channel = get_rabbitmq_connection()

    # Publish a message
    message = {"user_id": "123", "action": action, "timestamp": "2024-08-28T12:00:00Z"}
    channel.basic_publish(exchange='user_auth_exchange', routing_key='user.auth', body=str(message))

    connection.close()
