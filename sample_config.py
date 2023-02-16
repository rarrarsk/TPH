import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6142809779:AAH9wKCjuZVAvG1MNEFOYk22xLHHvZoBRi8")

    APP_ID = int(os.environ.get("APP_ID", 8233223))

    API_HASH = os.environ.get("API_HASH", "dacf95e444cf26fb3d7e9b997e3ee456")
