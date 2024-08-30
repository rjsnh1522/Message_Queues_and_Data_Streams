import sys
import os
import time

from conn import get_rabbitmq_connection


def main():
    connection, channel = get_rabbitmq_connection()

    channel.queue_declare(queue='hello')


    # def callback(ch, method, properties, body):
    #     # print(f" [x] Received {ch}" )
    #     # print(f" [x] Received {method}")
    #     # print(f" [x] Received {properties}")
    #     print(f" [x] Received {body}")
    #
    #
    # channel.basic_consume(queue='hello',
    #                       on_message_callback=callback,
    #                       auto_ack=True)
    # auto_ack=True would mark message delivered automatically so when
    # a worker dies message may get lost, so we should ack only when task is done.
    # in by default there is 30 minutes (we can increase the time too) to receive the ack if not
    # message would be stored if there is no worker if there is worker message will be sent to
    # the live worker.

    # manually doing the ack

    def callback(ch, method, properties, body):
        # print(f" [x] Received {ch}" )
        # print(f" [x] Received {method}")
        # print(f" [x] Received {properties}")
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(f" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # this is to make sure one worker gets only one message
    # till it process the current one, because RQ sends message as round robin
    # so one worker can get all the heavy tasks,
    # so it's better to send message to the worker only if it finishes the current task

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue',
                          on_message_callback=callback)



    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)