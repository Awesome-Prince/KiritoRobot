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

import logging
import os

import requests
from telethon import Button, events

from KiritoRobot import tbot
from KiritoRobot.anime_helper.other import conv_to_jpeg, format_results
from KiritoRobot.anime_helper.search import GRAPHQL, anime_query

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


@tbot.on(events.NewMessage(incoming=True, pattern="/anime ?(.*)"))
async def anime(event):
    input_str = event.pattern_match.group(1)
    ing = await tbot.send_message(
        event.chat_id, f"__Searching for__ `{input_str}` __in Anilist__"
    )
    variables = {"search": input_str}
    json = (
        requests.post(GRAPHQL, json={"query": anime_query, "variables": variables})
        .json()["data"]
        .get("Media", None)
    )
    if json:
        msg, info, trailer, image = format_results(json)
        if trailer:
            buttons = [
                [
                    Button.url("More Info", url=info),
                    Button.url("Trailer 🎬", url=trailer),
                ]
            ]
        else:
            buttons = [[Button.url("More Info", url=info)]]
        if image:
            try:
                namae = conv_to_jpeg(image)
                await AnimeBot.send_file(
                    event.chat_id,
                    namae,
                    caption=msg,
                    buttons=buttons,
                    reply_to=event.id,
                    force_document=False,
                )
                await ing.delete()
                os.remove(namae)
            except:
                msg += f" [\u2063]({image})"
                await ing.edit(msg, buttons=buttons)

@tbot.on(events.callbackquery.CallbackQuery(data="anime"))
async def _(event):
    await event.edit(CLEANER_HELP, buttons=[[Button.inline("◀ 𝖡𝖺𝖼𝗄", data="help")]])
