import json
import os

ENV_FILENAME = 'config.json'
ENV_VARIABLES = ['ACCESS_TOKEN', 'CLIENT_ID', 'BOT_NICK']


def get_config():
    with open(ENV_FILENAME) as f:
        config = json.load(f)
    for variable in ENV_VARIABLES:
        if not config.get(variable, ''):
            config[variable] = os.environ.get(variable)
    return config
