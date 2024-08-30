from rabbit.instagram_EDA.rabbit import get_rabbitmq_connection


def setup_user_auth_exchange():
    connection, channel = get_rabbitmq_connection()

    # Declare a direct exchange
    channel.exchange_declare(exchange='user_auth_exchange', exchange_type='direct')

    # Declare a queue
    channel.queue_declare(queue='user_auth_queue')

    # Bind the queue to the exchange with a routing key
    channel.queue_bind(exchange='user_auth_exchange', queue='user_auth_queue', routing_key='user.auth')

    connection.close()

# Initialize the exchange and queue
setup_user_auth_exchange()
