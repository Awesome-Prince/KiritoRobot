# By < @Awesome_Prince >
# // @BlackLoverNeterk //

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

BlackLover = TelegramClient('BlackLover', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
