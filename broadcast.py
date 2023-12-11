import pika

from utils.get_cities import get_city_temperatures


city_temperatures = get_city_temperatures()
exchange_name = 'weather-broadcaster'

conn = pika.BlockingConnection(pika.ConnectionParameters())
channel = conn.channel()
channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

for city in city_temperatures:
    channel.basic_publish(exchange=exchange_name,
                          routing_key=f'{city["continent"]}.{city["country"]}.{city["city"]}',
                          body=str(city['temperature']))
