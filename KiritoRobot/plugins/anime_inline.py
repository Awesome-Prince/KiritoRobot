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

import requests
from telethon import Button, events
from telethon.tl.functions.messages import SetInlineBotResultsRequest
from telethon.tl.types import (
    DocumentAttributeImageSize,
    InputBotInlineMessageMediaAuto,
    InputBotInlineResult,
    InputWebDocument,
)

from KiritoRobot import tbot
from KiritoRobot.anime_helper.other import format_results
from KiritoRobot.anime_helper.search import GRAPHQL, anime_query


@tbot.on(events.InlineQuery(pattern="anime ?(.*)"))
async def inline_anime(event):
    builder = event.builder
    query = event.pattern_match.group(1)
    variables = {"search": query}
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
        results = builder.photo(file=image, text=msg, buttons=buttons)
        await event.answer([results] if results else None)


##########CRAPS####################


@tbot.on(events.InlineQuery(pattern="test ?(.*)"))
async def inline_test(event):
    query = event.pattern_match.group(1)
    variables = {"search": query}
    json = (
        requests.post(GRAPHQL, json={"query": anime_query, "variables": variables})
        .json()["data"]
        .get("Media", None)
    )
    if json:
        msg, info, trailer, image = format_results(json)
    results = [
        InputBotInlineResult(
            id=event.id,
            type="photo",
            send_message=InputBotInlineMessageMediaAuto(msg),
            title=json["title"]["romaji"],
            description="Nothin",
            url=info,
            thumb=InputWebDocument(
                url=image,
                size=42,
                mime_type="image/png",
                attributes=[DocumentAttributeImageSize(w=42, h=42)],
            ),
            content=InputWebDocument(
                url=image,
                size=42,
                mime_type="image/png",
                attributes=[DocumentAttributeImageSize(w=42, h=42)],
            ),
        )
    ]
    await AnimeBot(SetInlineBotResultsRequest(event.id, results=results, cache_time=0))


@tbot.on(events.InlineQuery(pattern="something ?(.*)"))
async def inline_test2(event):
    query = event.pattern_match.group(1)
    variables = {"search": query}
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
    builder = event.builder
    size = DocumentAttributeImageSize(w=42, h=42)
    results = []
    results.append(
        builder.article(
            title=json["title"]["romaji"],
            description=f"{json['format']} | {json.get('episodes', 'N/A')} Episodes",
            url=info,
            thumb=InputWebDocument(
                url=image, size=42, attributes=size, mime_type="image/png"
            ),
            content=InputWebDocument(
                url=image, size=42, attributes=size, mime_type="image/png"
            ),
            text=msg,
            buttons=buttons,
        )
    )
    await event.answer(results if results else None)
