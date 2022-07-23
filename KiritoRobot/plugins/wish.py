import random
from PIL import Image
from KiritoRobot import tbot
from telethon import events
@tbot.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):

 if e.is_reply:
         mm = random.randint(1,100)
         lol = await e.get_reply_message()
         fire = "https://telegra.ph/file/049090e104b219c9db580.mp4"
         await tbot.send_file(e.chat_id, fire,caption=f"**Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your wish has been cast.🖤**\n\n__chance of success {mm}%__", reply_to=lol)
 if not e.is_reply:
         fire = "https://telegra.ph/file/049090e104b219c9db580.mp4"
         await tbot.send_file(e.chat_id, fire,caption=f"**MF [{e.sender.first_name}](tg://user?id={e.sender.id}), tell me your fuking wish first.**\n\n__go and ask your mom to how to fuck__", reply_to=e)
