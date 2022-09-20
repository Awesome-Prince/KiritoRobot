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

from KiritoRobot.anime_helper.search import shorten


def conv_to_jpeg(image):
    response = requests.get(image)
    file_name = "anilist.jpg"
    file = open(file_name, "wb")
    file.write(response.content)
    file.close()
    return file_name


def format_results(json):
    msg = f"""
**{json['title']['romaji']}**(`{json['title']['native']}`)
**Type**: {json['format']}
**Status**: {json['status']}
**Episodes**: {json.get('episodes', 'N/A')}
**Duration**: {json.get('duration', 'N/A')} Per Ep.
**Score**: {json['averageScore']}
**Genres**: `
"""
    for x in json["genres"]:
        msg += f"{x}, "
    msg = msg[:-2] + "`\n"
    msg += "**Studios**: `"
    for x in json["studios"]["nodes"]:
        msg += f"{x['name']}, "
    msg = msg[:-2] + "`\n"
    info = json.get("siteUrl")
    trailer = json.get("trailer", None)
    if trailer:
        trailer_id = trailer.get("id", None)
        site = trailer.get("site", None)
        if site == "youtube":
            trailer = "https://youtu.be/" + trailer_id
    description = (
        json.get("description", "N/A")
        .replace("<i>", "")
        .replace("</i>", "")
        .replace("<br>", "")
    )
    msg += shorten(description, info)
    image = info.replace("anilist.co/anime/", "img.anili.st/media/")
    return msg, info, trailer, image
