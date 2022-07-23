# By < @Awesome-Prince >
# // @BlackLoverNetwork //
from telethon import Button, events

from KiritoRobot.utils import KiritoRobot


@KiritoRobot(pattern=("/start"))
async def start(event):
    await event.reply(
        "Suprise Suprise Mother Fucker, The King Is Back[!](https://telegra.ph/file/36dd96df77bc2b7ef9b3d.png)",
        buttons=[
            [Button.url("Support", url="https://t.me/blacklover_support")],
            [Button.inline("Help", data="help")],
        ],
    )


@tbot.on(events.callbackquery.CallbackQuery(data="help"))
async def ex(event):
    await event.edit("Bot is under Development!")
