from time import sleep
import requests
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.sync import TelegramClient , functions , events
import asyncio
import random
import time
import os
import base64
id='5229914714'
token='6183317549:AAGB5jAoTSGSc0M0Y_8WR7kEa7oYbyjshM0'
led=TelegramClient('3z', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
led.start()
led.send_message('me','ok')
uss='qwertyuioplkjhgfdsazxcvbnm1234567890'
rr='qwertyuioplkjhgfdsazxcvbnm'

user = input('l  .  ? ')
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
            take = led(UpdateUsernameRequest(user))
            if take:
                requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text=« new hutting """)
        else:
            print(f"NOOO : {user}" + ' ' + str(i) + " " + str(x))