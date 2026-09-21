from __future__ import annotations

import asyncio

from discord import ClientException, FFmpegPCMAudio, Game, Intents, VoiceClient, utils
from discord.ext.commands import Bot, Cog, Context, command, has_permissions

from secret import token

AUDIO = "song.mp3"
FFMPEG = "/usr/bin/ffmpeg"
CHANNEL = "Doot Land"
NO_CHANNEL = "There is no **{}** voice channel. Make one and try again."
NOT_CONNECTED = "I'm not dooting anywhere right now."


intents = Intents.default()
intents.message_content = True

bot = Bot(
    command_prefix="?",
    help_command=None,
    activity=Game("DOOTING"),
    intents=intents,
)


class Doot(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        self.vc: VoiceClient | None = None

    @staticmethod
    def _source() -> FFmpegPCMAudio:
        return FFmpegPCMAudio(executable=FFMPEG, source=AUDIO)

    def _play(self, vc: VoiceClient) -> None:
        vc.play(self._source(), after=self._after)

    def _after(self, error: Exception | None) -> None:
        if error is not None:
            return

        vc = self.vc
        if vc is not None and vc.is_connected():
            self._play(vc)

    @command()
    async def play(self, ctx: Context[Bot]) -> None:
        if ctx.guild is None:
            return

        channel = utils.get(ctx.guild.voice_channels, name=CHANNEL)
        if channel is None:
            _ = await ctx.send(NO_CHANNEL.format(CHANNEL))
            return

        vc = ctx.guild.voice_client
        try:
            if isinstance(vc, VoiceClient) and vc.is_connected():
                await vc.move_to(channel)
            else:
                vc = await channel.connect()
        except (ClientException, asyncio.TimeoutError):
            return

        self.vc = vc
        if not vc.is_playing():
            self._play(vc)

    @command()
    @has_permissions(administrator=True)
    async def leave(self, ctx: Context[Bot]) -> None:
        vc = self.vc
        if vc is None or not vc.is_connected():
            _ = await ctx.send(NOT_CONNECTED)
            return

        self.vc = None
        await vc.disconnect()


async def main() -> None:
    utils.setup_logging()
    async with bot:
        await bot.add_cog(Doot(bot))
        await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
