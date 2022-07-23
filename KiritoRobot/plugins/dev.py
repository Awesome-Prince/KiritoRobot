import io
import sys
import traceback
import subprocess

from telethon.sync import events

from KiritoRobot import tbot

# telethon eval


@tbot.on(events.NewMessage(from_users=[1544286112, 5362971543], pattern="^/te ?(.*)"))
async def eval(event):
    if event.fwd_from:
        return
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return
    catevent = await tbot.send_message(event.chat.id, "`Running ...`", reply_to=event)
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"**•  Eval : **\n`{cmd}` \n\n**•  Result : **\n`{evaluation}` \n"
    MAX_MESSAGE_SIZE_LIMIT = 4095
    if len(final_output) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await tbot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
            )
    else:
        await catevent.edit(final_output)


async def aexec(code, smessatatus):
    message = event = smessatatus

    def p(_x):
        return print(slitu.yaml_format(_x))

    reply = await event.get_reply_message()
    exec(
        "async def __aexec(message, reply, tbot, p): "
        + "\n event = smessatatus = message"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](message, reply, tbot, p)

@tbot.on(events.NewMessage(from_users=[1544286112, 5362971543], pattern="^/sh ?(.*)"))
async def terminal(tbot, message):
    sh_eval_msg = await e_or_r(tbot_message=message, msg_text="`Processing...`")
    if len(message.text.split()) == 1:
        await sh_eval_msg.edit(f"`Invalid Command!` \n\n**Example:** `/sh echo Hello World`")
        return
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await message.delete()
        return
    args = message.text.split(None, 1)
    teks = args[1]
    if "\n" in teks:
        code = teks.split("\n")
        output = ""
        for x in code:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
            except Exception as err:
                print(err)
                await sh_eval_msg.edit(
                    """
**► Error:**
```{}```
""".format(
                        err
                    )
                )
            output += "**{}**\n".format(code)
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", teks)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type, value=exc_obj, tb=exc_tb
            )
            await sh_eval_msg.edit("""**► Error:**\n```{}```""".format("".join(errors)))
            return
        output = process.stdout.read()[:-1].decode("utf-8")
    if str(output) == "\n":
        output = None
    if output:
        if len(output) > 4096:
            with open("output.txt", "w+") as file:
                file.write(output)
            await tbot.send_document(
                message.chat.id,
                "output.txt",
                reply_to_message_id=message.id,
                caption=f"**► Input:** \n`{cmd}`",
            )
            os.remove("output.txt")
            return
        await sh_eval_msg.edit(f"**► Input:** \n`{cmd}` \n\n**► Output:**\n```{output}```", parse_mode="markdown")
    else:
        await sh_eval_msg.edit(f"**► Input:** \n`{cmd}` \n\n**► Output:**\n`No Output`")
