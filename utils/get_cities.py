import random

from utils.city_list import cities_data


def get_city_temperatures():
    ''' we assume there's an api behind this function that returns temperatures for each city '''

    return [
        dict(city, **{'temperature': round(random.uniform(-15, 40), 2)})
        for city in cities_data
    ]
