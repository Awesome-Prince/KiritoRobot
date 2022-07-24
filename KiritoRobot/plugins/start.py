# By < @Awesome-Prince >
# // @BlackLoverNetwork //
from KiritoRobot import tbot
from telethon import events, Button

PM_START_TEXT = """
huh
"""

@tbot.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("System Call", data="help")],
        [Button.url("Report Error", "https://t.me/BlackLover_Support")]])
       return

    if event.is_group:
       await event.reply("**System Is Alive!**")
       return
