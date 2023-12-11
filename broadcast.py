import pika
import json
import time

from utils.get_cities import get_city_temperatures

BROACAST_FREQUENCY_MP = 5
exchange_name = 'weather-broadcaster'

conn = pika.BlockingConnection(pika.ConnectionParameters())
channel = conn.channel()
channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

while True:
    city_temperatures = get_city_temperatures()

    for city in city_temperatures:
        topic_routing_key = f'{city["continent"]}.{city["country"]}.{city["city"]}'
        message = json.dumps(city)

        channel.basic_publish(exchange=exchange_name,
                              routing_key=topic_routing_key,
                              body=message)

    time.sleep(BROACAST_FREQUENCY_MP)
