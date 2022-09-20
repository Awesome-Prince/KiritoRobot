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

from telethon import Button, events, types

from KiritoRobot import tbot
from KiritoRobot.status import *

PINS_TEXT = """
**🎮 All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!**

➛ `/pin` - To pinned a reply msg.
➛ `/unpin` - To Unpin the latest pinned msg.
➛ `/unpinall` - To unpinall all pinned msgs at once.
➛ `/pinned` - To get current pinned msg.

**❍ Note:** __Add `notify` after /pin to notify all chat members.__
"""


@tbot.on(events.NewMessage(pattern="^[?!/]pinned"))
async def get_pinned(event):
    chat_id = (str(event.chat_id)).replace("-100", "")

    Ok = await tbot.get_messages(event.chat_id, ids=types.InputMessagePinned())
    tem = f"The pinned message in {event.chat.title} is <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
    await event.reply(tem, parse_mode="html", link_preview=False)


@tbot.on(events.NewMessage(pattern="^[!?/]pin ?(.*)"))
@is_admin
async def pin(event, perm):
    if not perm.pin_messages:
        await event.reply(
            "You are missing the following rights to use this command:CanPinMsgs."
        )
        return
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("Reply to a msg to pin it!")
        return
    input_str = event.pattern_match.group(1)
    if "notify" in input_str:
        await tbot.pin_message(event.chat_id, msg, notify=True)
        return
    await tbot.pin_message(event.chat_id, msg)


@tbot.on(events.NewMessage(pattern="^[!?/]unpin ?(.*)"))
@is_admin
async def unpin(event, perm):
    if not perm.pin_messages:
        await event.reply(
            "You are missing the following rights to use this command:CanPinMsgs."
        )
        return
    (str(event.chat_id)).replace("-100", "")
    ok = await tbot.get_messages(event.chat_id, ids=types.InputMessagePinned())
    await tbot.unpin_message(event.chat_id, ok)
    await event.reply(
        f"Successfully unpinned [this](t.me/{event.chat.username}/{ok.id}) message.",
        link_preview=False,
    )


@tbot.on(events.NewMessage(pattern="^[!?/]permapin"))
@is_admin
async def permapin(event, perm):
    if not perm.pin_messages:
        await event.reply(
            "You are missing the following rights to use this command:CanPinMsgs."
        )
        return
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("Reply to a msg to permapin it.")
        return
    hn = await tbot.send_message(event.chat_id, msg.message)
    await tbot.pin_message(event.chat_id, hn, notify=True)


@tbot.on(events.NewMessage(pattern="^[!?/]unpinall"))
async def unpinall(event, perm):
    if not perm.pin_messages:
        await event.reply(
            "You are missing the following rights to use this command:CanPinMsgs!"
        )
        return
    UNPINALL = """
Are you sure you want to 
unpin all msgs?
This action can't be undone!
"""

    await tbot.send_message(
        event.chat_id,
        UNPINALL,
        buttons=[
            [Button.inline("Confirm", data="unpin")],
            [Button.inline("Cancel", data="cancel")],
        ],
    )


@tbot.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await tbot.unpin_message(event.chat_id)
        await event.edit("Unpinned All Msgs!")
        return

    await event.answer("Group Creator Required!")


@tbot.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):

    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("Unpinning of all msgs has been cancelled!")
        return

    await event.answer("Group Creator Required!")


@tbot.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):

    await event.edit(PINS_TEXT, buttons=[[Button.inline("◀ 𝖡𝖺𝖼𝗄", data="help")]])
