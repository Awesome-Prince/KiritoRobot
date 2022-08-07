from telethon import Button, events

from KiritoRobot import tbot
from KiritoRobot.Configs import Config

btn = [
    [Button.inline("Admin", data="admin"), Button.inline("Bans", data="bans")],
    [Button.inline("Pins", data="pins"), Button.inline("Pugres", data="purges")],
    [Button.inline("Locks", data="locks"), Button.inline("UserInfo", data="userinfo")],
    [Button.inline("Zombies", data="zombies")],
]

HELP_TEXT = """
Hey There! This Is Kirito Again
━━━━━━━━━━━━━━━━━━━━━━━━
Tʀᴜsᴛ ɪɴ ᴍʏ ⚔️ AɪɴCʀᴀᴅ Sᴡᴏʀᴅ Sᴛʏʟᴇ ⚔️...
━━━━━━━━━━━━━━━━━━━━━━━━
System Commands Available:
❍ /start: Cʜᴇᴄᴋ Mᴇ... Iꜰ I Aᴍ Aʟɪᴠᴇ Oʀ Nᴏᴛ
❍ /help: Usᴇ Tʜɪs... Iꜰ Yᴏᴜ Nᴇᴇᴅ Mᴏʀᴇ Iɴꜰᴏ Aʙᴏᴜᴛ Mᴇ!
━━━━━━━━━━━━━━━━━━━━━━━━
For Issues Report At @BlackLover_Support
Powered by @BlackLover_Network [🖥](https://telegra.ph/file/b7d0d2c10a56e3b739611.png)
━━━━━━━━━━━━━━━━━━━━━━━━
All commands can either be used with /.

And the following:
"""


@tbot.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):

    if event.is_group:
        await event.reply(
            "Contact me in DM to get System Menu!",
            buttons=[
                [Button.url("System Call", "T.me/{}?start=help".format(Config.BOT_US))]
            ],
        )
        return

    await event.reply(HELP_TEXT, buttons=btn)


@tbot.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)


@tbot.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

    await event.edit(HELP_TEXT, buttons=btn)
