import discord
from discord.ext import commands


class Voice(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    async def play(self, ctx: commands.Context[commands.Bot]):
        if ctx.guild is None:
            await ctx.send("This command only works in servers")
            return

        voice_channel = discord.utils.get(ctx.guild.voice_channels, name="Doot Land")
        if voice_channel is None:
            await ctx.send("No voice channel named **Doot Land** found.")
            return

        try:
            voice_client = await voice_channel.connect()
        except discord.ClientException:
            return

        self.play_song(voice_client)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def leave(self, ctx: commands.Context[commands.Bot]):
        if ctx.voice_client:
            await ctx.voice_client.disconnect(force=True)
        else:
            await ctx.send("I am not in a voice channel")

    def play_song(self, voice_client: discord.VoiceClient):
        try:
            voice_client.play(
                discord.FFmpegPCMAudio("assets/song.mp3"),
                after=lambda e: self.play_song(voice_client),
            )
        except discord.ClientException:
            return
