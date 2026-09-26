from discord.ext import commands


class Voice(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context[commands.Bot]):
        await ctx.send("Hello")
