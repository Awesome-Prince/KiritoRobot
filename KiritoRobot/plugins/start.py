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
from KiritoRobot.utils import swordinline

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
        await event.reply(
            PM_START_TEXT.format(event.sender.first_name),
            buttons = [
    [Button.url("Add To Your Guild", "https://t.me/KiritoXProBot?startgroup=true")],
    [
        Button.inline("Terms And Conditions", data="tc"),
        Button.url("Error Report", "https://t.me/Programmer_Support"),
    ],
    [Button.inline("System Call", data="help")],
]

        return

    if event.is_group:
        await event.reply("**System Is Alive!**")
        return
           
@swordinline(pattern="tc")
async def t_c(e):
    buttons = Button.inline("Back", data="back")
    await e.edit(tc, buttons=buttons, link_preview=False)

@swordinline(pattern=r"back")
async def _(event):
    btn = [
    [Button.url("Add To Your Guild", "https://t.me/KiritoXProBot?startgroup=true")],
    [
        Button.inline("Terms And Conditions", data="tc"),
        Button.url("Error Report", "https://t.me/Programmer_Support"),
    ],
    [Button.inline("System Call", data="help")],
]

    await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=btn)
