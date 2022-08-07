import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
    BOT_US = os.environ.get("BOT_US", "BlackLover_Robot")
    WELCOME_TEXT = os.environ.get(
        "WELCOME_TEXT", "Cardinal System Is Damaged!, Sorry I Cant Remember You."
    )
    RULES = os.environ.get("RULES", "https://t.me/BlackLover_Updates/8")
