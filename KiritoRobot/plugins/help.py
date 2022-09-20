"""
BSD 2-Clause License

Copyright (c) 2022, Awesome-Prince (https://github.com/Awesome-Prince)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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
For Issues Report At @Programmer_Support
Powered by @Besties_XD [🖥](https://telegra.ph/file/b7d0d2c10a56e3b739611.png)
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
