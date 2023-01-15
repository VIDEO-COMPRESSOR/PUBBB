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
BOT_TOKEN = "5906335090:AAH3LPyJFhqqVRoeBZGR6wyQ67rViSA_f8U"
SESSION = "BQBytROVbjeojI8M_oCxYoqYgKV-yJX_RWGvbMjsWVsXe3TJQ3vl4Q4GBKXOye-0Fysb28KjqOGYxaG0h1c9g3yqCntENFSSic03e26DKH3GNNrLI9k1F3kz5alacSsKVav0RAxTfLyHnIfUSS66ZmjiEK2IShJNZD1w9GYT_cbv_BUhcY1VNs6lcd6WEEaP30oN8EjWIzSVajI9CS7o2jUmfzvVDXZ4HwPldSpXULZ943hE2yjr42cf1GRkilH-EWCloogGzFjcDg3FNJ7n_JpWxTbJDscGre3BM1Zi-v3o96kznNfFMTAVfMuERa60fHTZz8NaPe6riE4FhBVgz3VSJim92AA"
FORCESUB = "PREMIUM_USERS_KB"
AUTH = 5660434162


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
