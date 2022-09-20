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

from datetime import timedelta

from telethon import events

from KiritoRobot import tbot
from KiritoRobot.status import *


@tbot.on(events.NewMessage(pattern="[!?/]spam"))
@is_admin
async def spam(event, perm):
    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("That's not a user!")
        return
    ree = (await event.get_reply_message()).sender_id
    check = await tbot.get_permissions(event.chat_id, ree)

    if check.is_admin:
        await event.reply("He can be a spammer, but he is also an admin!")
        return
    elif check.is_creator:
        await event.delete()
        await event.reply("He is chat creator")
        return
    elif msg.sender.bot:
        await event.delete()
        await event.reply("Its a bot!")
        return

    re = (await event.get_reply_message()).sender_id
    user = await tbot.get_entity(ree)
    await event.delete()
    await tbot.edit_permissions(
        event.chat_id, re, timedelta(hours=1), send_messages=False
    )
    await tbot.send_message(
        event.chat_id,
        f"[{user.first_name}](tg://user?id={re}) it looks like you are spamming the chat!\nAnd so has been muted for 1 hour",
    )
