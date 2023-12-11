import json

import pika

from utils.subscription_key_builder import subscription_key_builder


exchange_name = 'weather-broadcaster'
topic_subscription_keys = subscription_key_builder(json.load(open('./subscription.json', 'r')))

connection = pika.BlockingConnection(pika.ConnectionParameters())
channel = connection.channel()
channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

queue = channel.queue_declare('', exclusive=True)
queue_name = queue.method.queue

for topic_subscription_key in topic_subscription_keys:
    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name,
                       routing_key=topic_subscription_key)


def callback(ch, method, properties, body):
    print(body.decode())


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
