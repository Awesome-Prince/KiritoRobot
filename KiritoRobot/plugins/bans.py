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
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from KiritoRobot import tbot, OWNER_ID
from KiritoRobot.status import *

BANS_TEXT = """
**🎮 An Powerful Element To Destroy Your Enemies!**

➛ `/kickme` - To self Kick you from a chat.
➛ `/kick` - To kick someone from a chat.
➛ `/unban` - To unban a member from the chat.
➛ `/ban` - To Ban Someone from a chat.
➛ `/dban` - To delete the replied msg and bans the user.
➛ `/sban` - To delete the replied msg and kicks the user.
➛ `/skick` - To Delete Your msg and kicks the user 
➛ `/dkick` - To delete your msg and and kicks the replied user.
"""


@tbot.on(events.NewMessage(pattern="^[!?/]kick ?(.*)"))
@is_admin
async def kick(event, perm):

    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to kick him")
        return

    replied_user = msg.sender_id
    us = msg.sender.username
    info = await tbot.get_entity(us)
    await tbot.kick_participant(event.chat_id, input_str or replied_user)
    await event.reply(
        f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}"
    )


@tbot.on(events.NewMessage(pattern="^[!?/]kickme"))
async def kickme(event):

    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return

    check = await tbot.get_permissions(event.chat_id, event.sender_id)
    if check.is_admin:
        await event.reply("Sorry but I can't kick admins!")
        return

    await event.reply("Ok, as your wish")
    await tbot.kick_participant(event.chat_id, event.sender_id)


@tbot.on(events.NewMessage(pattern="^[!?/]ban ?(.*)"))
@is_admin
async def ban(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to ban him")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await tbot.get_entity(us)
    await tbot(
        EditBannedRequest(
            event.chat_id,
            replied_user,
            ChatBannedRights(until_date=None, view_messages=True),
        )
    )
    await event.reply(
        f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) in {event.chat.title}"
    )


@tbot.on(events.NewMessage(pattern="^[!?/]unban ?(.*)"))
@is_admin
async def unban(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to unban him")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await tbot.get_entity(us)
    await tbot(
        EditBannedRequest(
            event.chat_id,
            replied_user,
            ChatBannedRights(until_date=None, view_messages=False),
        )
    )
    await event.reply(
        f"Succesfully Unbanned [{info.first_name}](tg://user?id={replied_user}) in {event.chat.title}"
    )


@tbot.on(events.NewMessage(pattern="^[!?/]skick"))
@is_admin
async def skick(event, perm):
    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete it and kick the user!")
        return

    us = reply_msg.sender.username
    info = await tbot.get_entity(us)
    x = (await event.get_reply_message()).sender_id
    (await event.get_reply_message())
    await event.delete()
    await tbot.kick_participant(event.chat_id, x)
    replied_user = reply_msg.sender_id
    await event.reply(
        f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}"
    )


@tbot.on(events.NewMessage(pattern="^[!?/]dkick"))
@is_admin
async def dkick(event, perm):
    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete it and kick the user!")
        return
    us = reply_msg.sender.username
    info = await tbot.get_entity(us)
    x = await event.get_reply_message()
    await x.delete()
    await tbot.kick_participant(event.chat_id, x.sender_id)
    replied_user = reply_msg.sender_id
    await event.reply(
        f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}"
    )


@tbot.on(events.NewMessage(pattern="^[!?/]dban"))
@is_admin
async def dban(event, perm):
    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete the message and ban the user!")
        return
    us = reply_msg.sender.username
    info = await tbot.get_entity(us)
    x = (await event.get_reply_message()).sender_id
    zx = await event.get_reply_message()
    await zx.delete()
    await tbot(
        EditBannedRequest(
            event.chat_id, x, ChatBannedRights(until_date=None, view_messages=True)
        )
    )
    replied_user = reply_msg.sender_id
    await event.reply("Successfully Banned!")
    await event.reply(
        f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}"
    )


@tbot.on(events.NewMessage(pattern="^[!?/]sban"))
@is_admin
async def sban(event, perm):
    if not perm.ban_users:
        await event.reply(
            "You are missing the following rights to use this command:CanBanUsers!"
        )
        return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete the message and ban the user!")
        return
    us = reply_msg.sender.username
    info = await tbot.get_entity(us)
    x = (await event.get_reply_message()).sender_id
    (await event.get_reply_message())
    await event.delete()
    await tbot(
        EditBannedRequest(
            event.chat_id, x, ChatBannedRights(until_date=None, view_messages=True)
        )
    )
    replied_user = reply_msg.sender_id
    await event.reply(
        f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}"
    )


@tbot.on(events.callbackquery.CallbackQuery(data="bans"))
async def banhelp(event):
    await event.edit(BANS_TEXT, buttons=[[Button.inline("◀ 𝖡𝖺𝖼𝗄", data="help")]])

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

@tbot.on(events.NewMessage(pattern="/banall$"))
async def banall(hmm):
    if not hmm.is_group:
        return
    if hmm.is_group:
        if hmm.sender_id != OWNER_ID:
            return
    await tbot.send_message(
        hmm.chat_id,
        "Are You Sure? Want To BanAll?",
        buttons=[
            [Button.inline("Confirm", data="banAll")],
            [Button.inline("Cancel", data="cancel")],
        ],
    )

@tbot.on(events.callbackquery.CallbackQuery(data="banAll"))
async def banAll(hmm):
    async for user in tbot.iter_participants(hmm.chat_id):
        try:
            await hmm.client(
                    EditBannedRequest(hmm.chat_id, user.id, BANNED_RIGHTS)
                )
        except:
            pass