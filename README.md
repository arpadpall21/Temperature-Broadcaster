# Weather-Broadcaster
Broadcasting temperature through RabbitMQ (topic exchange) 

- pika RabbitMQ client lib used
- the broadcaster broadcasts temperature info in topics <continent>.<country>.<city>
- the client subscribes to areas listed in `subscribe.json`


- venv suggestion