from rabbit.instagram_EDA.rabbit import get_rabbitmq_connection


def setup_user_post_exchange():
    connection, channel = get_rabbitmq_connection()

    # Declare a fanout exchange
    channel.exchange_declare(exchange='user_post_exchange', exchange_type='fanout')

    # Declare queues
    channel.queue_declare(queue='post_service_queue')
    channel.queue_declare(queue='notification_service_queue')

    # Bind queues to the exchange
    channel.queue_bind(exchange='user_post_exchange', queue='post_service_queue')
    channel.queue_bind(exchange='user_post_exchange', queue='notification_service_queue')

    connection.close()


def setup_like_exchange():
    connection, channel = get_rabbitmq_connection()

    # Declare a topic exchange
    channel.exchange_declare(exchange='like_exchange', exchange_type='topic')

    # Declare queues
    channel.queue_declare(queue='like_service_queue')
    channel.queue_declare(queue='analytics_service_queue')

    # Bind queues to the exchange with routing keys
    channel.queue_bind(exchange='like_exchange', queue='like_service_queue', routing_key='post.like')
    channel.queue_bind(exchange='like_exchange', queue='analytics_service_queue', routing_key='post.like')

    connection.close()

# Initialize the exchange and queues
setup_user_post_exchange()
setup_like_exchange()