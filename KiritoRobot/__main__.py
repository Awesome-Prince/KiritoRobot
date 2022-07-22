# Work Done By < @Awesome-Prince >
# // @BlackLoverNetwork //

import glob
import logging
from pathlib import Path

from KiritoRobot.utils import load_plugins

from . import KiritoRobot

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

path = "KiritoRobot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Your Host Is Successfully Done!")
print("Visit @BlackLover_Support if any error")
if __name__ == "__main__":
    BlackLover.run_until_disconnected()
