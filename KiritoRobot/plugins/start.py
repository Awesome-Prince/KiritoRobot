# By < @Awesome-Prince >
# // @BlackLoverNetwork //
from .. import BlackLover
from telethon import events, Button

@BlackLover.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Suprise Suprise Mother Fucker, The King Is Back!",
                    buttons=[
                        [Button.url("Support", url="https://t.me/blacklover_support")],
                        [Button.inline("Help",data="help")]
                    ])

@BlackLover.on(events.callbackquery.CallbackQuery(data="help"))
async def ex(event):
    await event.edit("Bot is under Development!")
