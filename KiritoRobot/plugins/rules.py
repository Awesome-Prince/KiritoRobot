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
