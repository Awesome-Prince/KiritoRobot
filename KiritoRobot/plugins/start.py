# By < @Awesome-Prince >
# // @BlackLoverNetwork //
from telethon import Button, events

from KiritoRobot import KiritoRobot


@KiritoRobot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(
        "Suprise Suprise Mother Fucker, The King Is Back!",
        buttons=[
            [Button.url("Support", url="https://t.me/blacklover_support")],
            [Button.inline("Help", data="help")],
        ],
    )


@KiritoRobot.on(events.callbackquery.CallbackQuery(data="help"))
async def ex(event):
    await event.edit("Bot is under Development!")
