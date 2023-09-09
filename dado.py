import httpx
from time import sleep; import requests
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon import TelegramClient , functions
import asyncio
user = 'iiiidida'
x = 0
for t in range(3333):
    i = 0
    for t in range(3333):
        i += +1
        x += +1
        sleep(0.0001)
        if i == 270:
            sleep(2)
            break
        req = httpx.get(f"https://t.me/{user}")
        if ('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') in req.text :
            print('yes')
            sleep(50000)
        else:
            print(f"NOOO : {user}" + ' ' + str(i) + " " + str(x))
