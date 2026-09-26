from typing import override

import discord
from discord.ext import commands

from doot_bot.cogs.voice import Voice


class DootBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="?", intents=intents)

    @override
    async def setup_hook(self) -> None:
        await self.add_cog(Voice(self))

    async def on_ready(self):
        print(f"Logged in as {self.user}")
