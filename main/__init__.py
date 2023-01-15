#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 7498895
API_HASH = "5204d72f395c291b7257df9631a659ee"
BOT_TOKEN = "5483606285:AAFnhGmxdlR-kGp6tm8zo9zsyFmQ7dOoVQk"
SESSION = "BQAOzPBvBI95y0q-BUam1l_i88rLcGiqAyiyUMyp7cXE9IcBlM4vysguJSXYHV7iPSJVfebmA3bcz_8f9azL9hgSXbqFb6GlepGTI3eZom8tkLzekfto7mB9DOFewi9QplyqFEhgqysoGhSkngw2-qAuyoj5ZOhdPV651NcP9839akAXuibSDpYZzLkZaIuAYzE464yJEAhMQFByNb_epcfdu_9Mx5P7HEh-IIfLhYKOAoB5xYyggjTsXg8cdFb4L6YbhAF0QVmM-Qdrtxf4wHnFr2LvTWlNcaddVX1HCIcKL4Yd7u49639K5DvVaggBY29JgYAi1ZnhdXb2RhfIsgPUYOwEmQA"
FORCESUB = "PREMIUM_USERS_KB"
AUTH = 5429507511


bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
