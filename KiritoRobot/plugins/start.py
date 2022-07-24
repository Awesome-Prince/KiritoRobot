# By < @Awesome-Prince >
# // @BlackLoverNetwork //
from KiritoRobot import tbot
from telethon import events, Button

PM_START_TEXT = """
────「 [Kirito Robot 키리토](https://telegra.ph/file/36dd96df77bc2b7ef9b3d.png) 」────
**Hola! {},
I am an Anime themed advance group management bot with a lot of Cool Features.**
➖➖➖➖➖➖➖➖➖➖➖➖➖
➛ Use System Call Command Below To Know My Abilities ××
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
