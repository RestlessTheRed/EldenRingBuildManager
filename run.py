import os

from config import get_config


if __name__ == '__main__':
    config = get_config()
    for param in ['ER_INVENTORY_API_URL', 'ER_INVENTORY_AUTH_TOKEN']:
        os.environ[param] = config[param]
    from bot import Bot
    bot = Bot(
        token=config['ACCESS_TOKEN'],
        client_id=config['CLIENT_ID'],
        nick=config['BOT_NICK'].lower(),
        prefix=config['BOT_PREFIX'],
        initial_channels=[channel.lower() for channel in config['CHANNELS']],
    )
    bot.run()
