from . import TOKEN, tbot
import KiritoRobot.utils

try:
    tbot.start(bot_token=TOKEN)
except Exception as z:
    print(z)

tbot.run_until_disconnected()
print("Your Host Is Successfully Done!")
print("Visit @Programmer_Support if any error")
