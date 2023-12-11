def subscription_key_builder(locations: dict) -> [str]:
    topic_subscription_keys = []

    for location in locations:
        for place in locations[location]:
            if location == 'continents':
                topic_subscription_keys.append(f'{place}.*.*')
            elif location == 'countries':
                topic_subscription_keys.append(f'*.{place}.*')
            elif location == 'cities':
                topic_subscription_keys.append(f'*.*.{place}')

    return topic_subscription_keys
