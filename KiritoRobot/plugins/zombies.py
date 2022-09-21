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
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from KiritoRobot import tbot
from KiritoRobot.status import *

CLEANER_HELP = """
**🎮 An Powerful Element To Remove Deleted Accounts From Your Groups!**

➛ `/zombies` - To find zombies accounts in your chat.
➛ `/zombies clean` - To remove the deleted accounts from your chat.
"""


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@tbot.on(events.NewMessage(pattern="^[!?/]zombies ?(.*)"))
@is_admin
async def clean(event, perm):
    if not perm.ban_users:
        await event.reply("You don't have enough rights")
        return
    input_str = event.pattern_match.group(1)
    stats = "Group is clean."
    deleted = 0

    if "clean" not in input_str:
        zombies = await event.respond("Searching For Zombies/Deleted Accounts...")
        async for user in event.client.iter_participants(event.chat_id):

            if user.deleted:
                deleted += 1
        if deleted > 0:
            stats = f"Found **{deleted}** Zombies In This Group.\
            \nClean Them By Using - `/zombies clean`"
        await zombies.edit(stats)
        return

    cleaning_zombies = await event.respond("Cleaning Zombies/Deleted Accounts...")
    del_u = 0
    del_a = 0

    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            try:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await cleaning_zombies.edit("I Don't Have Ban Rights In This Group.")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        stats = f"Cleaned `{del_u}` Zombies"

    if del_a > 0:
        stats = f"Cleaned `{del_u}` Zombies \
        \n`{del_a}` Zombie Admin Accounts Are Not Removed!"

    await cleaning_zombies.edit(stats)


@tbot.on(events.callbackquery.CallbackQuery(data="zombies"))
async def _(event):
    await event.edit(CLEANER_HELP, buttons=[[Button.inline("◀ 𝖡𝖺𝖼𝗄", data="help")]])
