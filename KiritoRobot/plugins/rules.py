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

RULES = Config.RULES


@tbot.on(events.NewMessage(pattern="^[!?/]rules"))
async def rules(event):

    msg = await event.get_reply_message()
    if not msg and event.is_group:
        await event.delete()
        await event.respond(
            "Please read the rules before chatting here!",
            buttons=[
                [Button.url("Rules", "t.me/{}?start=rules".format(Config.BOT_US))]
            ],
        )
        return

    re = (await event.get_reply_message()).id
    await event.delete()
    await tbot.send_message(
        event.chat_id,
        "Please read the rules before chatting here!",
        buttons=[[Button.url("Rules", "t.me/{}?start=rules".format(Config.BOT_US))]],
        reply_to=re,
    )
    return

    await event.reply(RULES)


@tbot.on(events.NewMessage(pattern="^/start rules"))
async def rules(event):

    if event.is_group:
        await event.reply(
            "Please read the rules before chatting here!",
            buttons=[
                [Button.url("Chat Rules", "t.me/{}?start=rules".format(Config.BOT_US))]
            ],
        )
        return

    await event.reply(RULES)


@tbot.on(events.callbackquery.CallbackQuery(data="rules"))
async def _(event):

    await event.edit(RULES, buttons=[[Button.inline("◀ 𝖡𝖺𝖼𝗄", data="start")]])
