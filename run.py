import os
import subprocess
import sys

from config import get_config


if __name__ == '__main__':
    try:
        import twitchio
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'twitchio'])
    config = get_config()
    for param, value in config.items():
        os.environ[param] = value
    from bot import Bot
    bot = Bot(
        token=os.environ['ACCESS_TOKEN'],
        client_id=os.environ['CLIENT_ID'],
        nick=os.environ['BOT_NICK'],
        prefix=os.environ['BOT_PREFIX'],
        initial_channels=[os.environ['CHANNEL']],
    )
    bot.run()
