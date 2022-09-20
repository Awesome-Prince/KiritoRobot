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
from KiritoRobot.status import *

LOCKS_HELP = """
**🎮 Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!**

➛ `/lock` - To lock a module in the chat.
➛ `/unlock` - To unlock a module in the chat.
➛ `/locktypes` - To get a list of modules can be locked
"""


@tbot.on(events.NewMessage(pattern="^[!?/]lock ?(.*)"))
@is_admin
async def lock(event, perm):
    if not perm.change_info:
        await event.reply(
            "You are missing the following rights to use this command:CanChangeInfo"
        )
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.reply("You haven't specified anything to lock.")
        return
    if "text" in input_str:
        await tbot.edit_permissions(event.chat_id, send_messages=False)
        await event.reply("Locked `text`.")
    elif "media" in input_str:
        await tbot.edit_permissions(event.chat_id, send_media=False)
        await event.reply("Locked `media`.")
    elif "sticker" in input_str:
        await tbot.edit_permissions(event.chat_id, send_stickers=False)
        await event.reply("Locked `sticker`.")
    elif "gifs" in input_str:
        await tbot.edit_permissions(event.chat_id, send_gifs=False)
        await event.reply("Locked `gifs`.")
    elif "forward" in input_str:
        await tbot.edit_permissions(event.chat_id, forwards=False)
        await event.reply("Locked `forward`.")
    elif "games" in input_str:
        await tbot.edit_permissions(event.chat_id, send_games=False)
        await event.reply("Locked `games`.")
    elif "inline" in input_str:
        await tbot.edit_permissions(event.chat_id, send_inline=False)
        await event.reply("Locked `inline`.")
    elif "polls" in input_str:
        await tbot.edit_permissions(event.chat_id, send_polls=False)
        await event.reply("Locked `polls`.")
    elif "preview" in input_str:
        await tbot.edit_permissions(event.chat_id, embed_link_previews=False)
        await event.reply("Locked `preview`.")
    elif "all" in input_str:
        await tbot.edit_permissions(
            event.chat_id,
            send_messages=False,
            send_media=False,
            send_stickers=False,
            send_gifs=False,
            send_games=False,
            send_inline=False,
            send_polls=False,
            embed_link_previews=False,
        )
        await event.reply("Locked `all`.")


@tbot.on(events.NewMessage(pattern="^[!?/]unlock ?(.*)"))
@is_admin
async def unlock(event, perm):
    if not perm.change_info:
        await event.reply(
            "You are missing the following rights to use this command:CanChangeInfo"
        )
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.reply("You haven't specified anything to unlock.")
        return
    if "text" in input_str:
        await tbot.edit_permissions(event.chat_id, send_messages=True)
        await event.reply("Unlocked `text`.")
    elif "media" in input_str:
        await tbot.edit_permissions(event.chat_id, send_media=True)
        await event.reply("Unlocked `media`.")
    elif "sticker" in input_str:
        await tbot.edit_permissions(event.chat_id, send_stickers=True)
        await event.reply("Unlocked `sticker`.")
    elif "gifs" in input_str:
        await tbot.edit_permissions(event.chat_id, send_gifs=True)
        await event.reply("Unlocked `gifs`.")
    elif "forward" in input_str:
        await tbot.edit_permissions(event.chat_id, forwards=True)
        await event.reply("Unlocked `forward`.")
    elif "games" in input_str:
        await tbot.edit_permissions(event.chat_id, send_games=True)
        await event.reply("Unlocked `games`.")
    elif "inline" in input_str:
        await tbot.edit_permissions(event.chat_id, send_inline=True)
        await event.reply("Unlocked `inline`.")
    elif "polls" in input_str:
        await tbot.edit_permissions(event.chat_id, send_polls=True)
        await event.reply("Unlocked `polls`.")
    elif "preview" in input_str:
        await tbot.edit_permissions(event.chat_id, embed_link_previews=True)
        await event.reply("Unlocked `preview`.")
    elif "all" in input_str:
        await tbot.edit_permissions(
            event.chat_id,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            send_polls=True,
            embed_link_previews=True,
        )
        await event.reply("Unlocked `all`.")


@tbot.on(events.NewMessage(pattern="^[!?/]locktypes"))
async def locktypes(event):
    TEXT = """
**Locks:**

➛ Text
➛ Media
➛ Sticker
➛ Gifs
➛ Videos
➛ Contacts
➛ Games
➛ Inline 
➛ all
"""
    await event.reply(TEXT)


@tbot.on(events.callbackquery.CallbackQuery(data="locks"))
async def _(event):

    await event.edit(LOCKS_HELP, buttons=[[Button.inline("◀ 𝖡𝖺𝖼𝗄", data="help")]])
