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


@tbot.on(events.CallbackQuery(pattern=r"check-bot-(\d+)"))
async def check(event):

    user_id = int(event.pattern_match.group(1))
    chat_id = event.chat_id
    if not event.sender_id == user_id:
        await event.answer("You can already speak freely!", alert=True)
        return
    if event.sender_id == user_id:
        await tbot.edit_permissions(chat_id, event.sender_id, send_messages=True)
        await event.answer("You are succesfully unmuted!")
        await event.edit(
            Config.WELCOME_TEXT,
            buttons=[
                [Button.url("Chat Rules!", "t.me/{}?start=rules".format(Config.BOT_US))]
            ],
            parse_mode="HTML",
            link_preview=False,
        )


@tbot.on(events.ChatAction)
async def join(event):

    if event.user_joined:
        await tbot.edit_permissions(event.chat_id, event.user_id, send_messages=False)
        await event.reply(
            Config.WELCOME_TEXT,
            parse_mode="HTML",
            link_preview=False,
            buttons=[
                [
                    Button.inline(
                        "Click Here To Unmute Yourslef!",
                        data=f"check-bot-{event.user_id}",
                    )
                ]
            ],
        )
