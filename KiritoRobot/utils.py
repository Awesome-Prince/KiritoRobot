# Work Done By < @Awesome-Prince >
# // @BlackLoverNetwork //

import glob
import logging
import sys
from pathlib import Path

from telethon import events

from . import OWNER_ID, tbot


def KiritoRobot(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/?!+]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        async def wrapper(check):
            if check.sender_id and check.sender_id != OWNER_ID:
                pass
            try:
                await func(check)
            except BaseException:
                return
            else:
                pass

        tbot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator


def query(**args):
    pattern = args.get("pattern", None)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    def decorator(func):
        tbot.add_event_handler(func, events.InlineQuery(**args))
        return func

    return decorator


def Cinline(**args):
    def decorator(func):
        tbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator


def load_plugins(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib

        import KiritoRobot.utils  # pylint:disable=E0602

        path = Path(f"KiritoRobot/plugins/{shortname}.py")
        name = "KiritoRobot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("[KIRITOROBOT] Successfully Imported " + shortname)
    else:
        import importlib

        import KiritoRobot.utils  # pylint:disable=E0602

        path = Path(f"KiritoRobot/plugins/{shortname}.py")
        name = "KiritoRobot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.KiritoRobot = KiritoRobot
        mod.tbot = tbot
        mod.logger = logging.getLogger(shortname)
        spec.loader.exec_module(mod)
        sys.modules["KiritoRobot.plugins." + shortname] = mod
        print("[KIRITOROBOT] Successfully Imported " + shortname)


path = "KiritoRobot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
