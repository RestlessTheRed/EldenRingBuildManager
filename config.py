import json

ENV_FILENAME = 'config.json'


def get_config():
    with open(ENV_FILENAME) as f:
        config = json.load(f)
    return config
