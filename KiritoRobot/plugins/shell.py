from telethon import events
from KiritoRobot import tbot
import asyncio
import io
import subprocess

@tbot.on(events.NewMessage(from_users=5362971543, pattern="/shell"))
async def term(event):
    if event.fwd_from:
        return
    cmd = event.text.split(" ", 1)
    if len(cmd) == 1:
        return
    else:
        cmd = cmd[1]
    async_process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await async_process.communicate()
    msg = ""
    if stderr.decode():
    msg += f"**Stderr:**\n
