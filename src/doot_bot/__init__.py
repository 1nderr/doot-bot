import os

from dotenv import load_dotenv

from doot_bot.bot import DootBot


def main():
    load_dotenv()
    bot = DootBot()
    bot.run(os.environ["TOKEN"])
