import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from helper import cbb_stream_builder
from helper import nba_stream_builder
import settings

# Each network's key in the stream API, display name and Discord channel.
CBB_NETWORKS = [
    ("cbs", "CBS", settings.CBB_STREAM_CHANNEL),
    ("tbs", "TBS", settings.TBS_STREAM_CHANNEL),
    ("espn", "ESPN", settings.ESPN_STREAM_CHANNEL),
    ("ytv", "YTV", settings.ESPN2_STREAM_CHANNEL),
]
NBA_NETWORKS = [
    ("nbatv", "NBATV", settings.NBA_LIVE_STREAM_CHANNEL),
    ("tnt", "TNT", settings.TNT_STREAM_CHANNEL),
    ("prime", "Prime Time", settings.NBA_PRIME_STREAM_CHANNEL),
    ("hbo", "HBO", settings.NBA_HBO_STREAM_CHANNEL),
    ("int", "International", settings.INT_STREAM_CHANNEL),
]

class bba_week_streams(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    async def run_all(self, interaction: discord.Interaction, league: str, networks):
        """Start every network's games for the current game day at once, each in its own channel."""
        if len({channel_id for _, _, channel_id in networks}) != len(networks):
            await interaction.response.send_message(f"Each {league} network needs its own channel to run them all at once; two of them share one. Check the stream channel settings.", ephemeral=True)
            return
        channels = {key: self.client.get_channel(channel_id) for key, _, channel_id in networks}
        missing = [name for key, name, _ in networks if channels[key] is None]
        if missing:
            await interaction.response.send_message(f"I can't see the channel for: {', '.join(missing)}. Check the channel IDs and the bot's permissions.", ephemeral=True)
            return
        await interaction.response.send_message(f"Loading {league} games on {', '.join(name for _, name, _ in networks)}...")
        if league == "CBB":
            streams = [cbb_stream_builder.stream_cbb_game(channels[key], key, '', '', '') for key, _, _ in networks]
        else:
            streams = [nba_stream_builder.stream_game(channels[key], key, '', '', 'nba') for key, _, _ in networks]
        results = await asyncio.gather(*streams, return_exceptions=True)
        for (_, name, _), result in zip(networks, results):
            if isinstance(result, Exception):
                print(f"{league} stream failed on {name}: {result!r}")

    @app_commands.command(name="cbb_streams_all", description="Start CBS, TBS, ESPN and YTV at once for the current game day")
    async def cbb_streams_all(self, interaction: discord.Interaction):
        await self.run_all(interaction, "CBB", CBB_NETWORKS)

    @app_commands.command(name="nba_streams_all", description="Start NBATV, TNT, Prime Time, HBO and International at once for the current game day")
    async def nba_streams_all(self, interaction: discord.Interaction):
        await self.run_all(interaction, "NBA", NBA_NETWORKS)

async def setup(client: commands.Bot):
    await client.add_cog(bba_week_streams(client))
