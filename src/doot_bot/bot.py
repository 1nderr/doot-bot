import discord
from discord.ext import commands


class DootBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="?", intents=intents)

    async def on_ready(self):
        print(f"Logged in as {self.user}")
