import json
import os

from config import get_config


if __name__ == '__main__':
    config = get_config()
    for param, value in config.items():
        if param in {'ER_INVENTORY_API_URL', 'ER_INVENTORY_AUTH_TOKEN'}:
            os.environ[param] = value
        if param == 'ER_INVENTORY_USER_IDS':
            channel2uid = {channel.lower(): uid for channel, uid in value.items()}
            os.environ[param] = json.dumps(channel2uid)
    from bot import Bot
    bot = Bot(
        token=config['ACCESS_TOKEN'],
        client_id=config['CLIENT_ID'],
        nick=config['BOT_NICK'].lower(),
        prefix=config['BOT_PREFIX'],
        initial_channels=[channel.lower() for channel in config['CHANNELS']],
    )
    bot.run()
