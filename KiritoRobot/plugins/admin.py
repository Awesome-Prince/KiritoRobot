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
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatAdminRights

from KiritoRobot import tbot
from KiritoRobot.status import *


@tbot.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("◀ 𝖡𝖺𝖼𝗄", data="help")]])


@tbot.on(events.NewMessage(pattern="^[!?/]promote ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups, not in PM!")
        return

    if not perm.add_admins:
        await event.reply(
            "You are missing the following rights to use this command:CanAddAdmins!"
        )
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("Reply to a user or give its username to promote him!")
        return
    sed = await tbot(GetFullUserRequest(id=user.sender_id or input_str))
    await tbot(
        EditAdminRequest(
            event.chat_id,
            user.sender_id or input_str,
            ChatAdminRights(
                add_admins=False,
                invite_users=True,
                change_info=False,
                ban_users=True,
                delete_messages=True,
                pin_messages=True,
            ),
            rank="Admin",
        )
    )

    if not input_str:
        await event.reply(
            f"Successfully Promoted [{sed.user.first_name}](tg://user?id={user.sender_id}) in {event.chat.title}!"
        )
        return

    await event.reply(f"Succesfully Promoted {input_str} in {event.chat.title}")


@tbot.on(events.NewMessage(pattern="^[!?/]superpromote ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups, not in PM!")
        return

    if not perm.add_admins:
        await event.reply(
            "You are missing the following rights to use this command:CanAddAdmins!"
        )
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("Reply to a user or give its username to promote him!")
        return
    sed = await tbot(GetFullUserRequest(id=user.sender_id or input_str))
    await tbot(
        EditAdminRequest(
            event.chat_id,
            user.sender_id or input_str,
            ChatAdminRights(
                add_admins=True,
                invite_users=True,
                change_info=True,
                ban_users=True,
                delete_messages=True,
                pin_messages=True,
            ),
            rank="BlackLover",
        )
    )

    if not input_str:
        await event.reply(
            f"Successfully SuperPromoted [{sed.user.first_name}](tg://user?id={user.sender_id}) in {event.chat.title}!"
        )
        return

    await event.reply(f"Succesfully SuperPromoted {input_str} in {event.chat.title}")


@tbot.on(events.NewMessage(pattern="^[!?/]safepromote ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups, not in PM!")
        return

    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("Reply to a user or give its username to promote him!")
        return
    sed = await tbot(GetFullUserRequest(id=user.sender_id or input_str))
    await tbot(
        EditAdminRequest(
            event.chat_id,
            user.sender_id or input_str,
            ChatAdminRights(
                add_admins=False,
                invite_users=True,
                change_info=False,
                ban_users=False,
                delete_messages=True,
                pin_messages=True,
            ),
            rank="Admin",
        )
    )

    if not input_str:
        await event.reply(
            f"Successfully Promoted [{sed.user.first_name}](tg://user?id={user.sender_id}) in {event.chat.title}!"
        )
        return

    await event.reply(f"Succesfully Promoted {input_str} in {event.chat.title}")


@tbot.on(events.NewMessage(pattern="^[!?/]demote ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups, not in PM!")
        return
    if not perm.add_admins:
        await event.reply(
            "You are missing the following rights to use this command:CanAddAdmins!"
        )
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("Reply to a user or give its username to demote him!")
        return
    sed = await tbot(GetFullUserRequest(id=user.sender_id or input_str))
    await tbot(
        EditAdminRequest(
            event.chat_id,
            user.sender_id or input_str,
            ChatAdminRights(
                add_admins=False,
                invite_users=None,
                change_info=None,
                ban_users=None,
                delete_messages=None,
                pin_messages=None,
            ),
            rank="Not Admin",
        )
    )

    if not input_str:
        await event.reply(
            f"Successfully Demoted [{sed.user.first_name}](tg://user?id={user.sender_id}) in {event.chat.title}!"
        )
        return

    await event.reply(f"Succesfully Demoted {input_str} in {event.chat.title}")


@tbot.on(events.NewMessage(pattern="^[!?/]invitelink"))
async def invitelink(event):

    if event.is_private:
        await event.reply("This cmd is made to be used in groups, not in PM!")
        return
    link = await tbot(ExportChatInviteRequest(event.chat_id))
    await event.reply(
        f"Group link of {event.chat.title} is [here]({link.link})", link_preview=False
    )


ADMIN_TEXT = """
**🎮 An Powerful Element For Increase Your Ranks!**

➛ `/promote` - To Promote a user in the chat.
➛ `/safepromote` - To Promote a user without ban rights.
➛ `/superpromote` - To Promote a user with full rights.
➛ `/demote` - To Demote a user in the chat.
➛ `/invitelink` - To get invitelink of a chat.
"""
