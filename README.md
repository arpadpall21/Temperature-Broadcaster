# Temperature Broadcasting

## Description
- This is a temperature broadcasting demo that used RabbitMQ as a message broker, for the demo's sake we are broadcasting every 5 seconds 
- The temperature is randomly generated (again for the demo's sake) at every broadcast 
- Producer (broadcaster):
  - Broadcasts temperatures for cities listed in `utils/city_list.py`
- Consumers (clients):
  - Can subscribe to locations: `continents`, `countries` or `cities` 
  - Subscriptions are hierarchy-based (ex: subscribing to the continent `North America` the client will get all cities on the continent)

## Setup
- install RabbitMQ:
  - the easiest way is to use Docker, run `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management`, this will download the RabbitMQ image and start the service in a Docker container (exiting the command will stop RabbitMQ and remove the container)
- Run `pip install -r requirements.txt` to install required packages (I recommend using a Python virtual environment)

## Usage
- Producer (broadcaster):
  - Run `python broadcast.py` to start broadcasting
- Consumers (clients):
  - Consumers use the `subscription.json` file to subscribe to the selected locations
  - Run `python client.py` to start receiving broadcasted messages
