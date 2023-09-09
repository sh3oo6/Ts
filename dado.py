from time import sleep; import requests
import time
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon import TelegramClient , functions
import asyncio
user = 'iiiidida'
x = 0
for t in range(3333):
    i = 0
    start_time = time.time()
    for t in range(3333):
        i += +1
        x += +1
        if i == 299:
            end_time = time.time()  # وقت انتهاء تنفيذ الكود
            execution_time = end_time - start_time  # الوقت المستغرق في تنفيذ الكود بالثواني
            print(f"الوقت المستغرق: {int(execution_time)} ثواني")
            sleep(61-int(execution_time))
            break
        req = requests.get(f"https://t.me/{user}")
        if ('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') in req.text :
            print('yes')
            sleep(50000)
        else:
            print(f"NOOO : {user}" + ' ' + str(i) + " " + str(x))
