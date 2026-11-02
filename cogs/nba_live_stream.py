import discord
from discord.ext import commands
from discord import app_commands
from helper import nba_stream_builder
import settings

nbatv_channel_id = settings.NBA_LIVE_STREAM_CHANNEL
tnt_channel_id = settings.TNT_STREAM_CHANNEL
int_channel_id = settings.INT_STREAM_CHANNEL
nba_prime_channel_id = settings.NBA_PRIME_STREAM_CHANNEL
nba_hbo_channel_id = settings.NBA_HBO_STREAM_CHANNEL

class nba_live_stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    nba_stream_group = app_commands.Group(name="nba_streams", description="Stream SimNBA Basketball Games")

    @nba_stream_group.command(name="nbatv", description="Stream the NBATV games")
    async def nbatv(self, interaction: discord.Interaction):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimNBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', '', '', 'nba')

    @nba_stream_group.command(name="tnt", description="Stream the TNT games")
    async def tnt(self, interaction: discord.Interaction):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimNBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', '', '', 'nba')

    @nba_stream_group.command(name="prime", description="Stream the Prime Time games")
    async def prime(self, interaction: discord.Interaction):
        chan = self.client.get_channel(nba_prime_channel_id)
        await interaction.response.send_message("Loading SimNBA Prime Time Games...")
        await nba_stream_builder.stream_game(chan, 'prime', '', '', 'nba')

    @nba_stream_group.command(name="hbo", description="Stream the HBO games")
    async def hbo(self, interaction: discord.Interaction):
        chan = self.client.get_channel(nba_hbo_channel_id)
        await interaction.response.send_message("Loading SimNBA HBO Games...")
        await nba_stream_builder.stream_game(chan, 'hbo', '', '', 'nba')

    @nba_stream_group.command(name="int", description="Stream the International games")
    async def int(self, interaction: discord.Interaction):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimNBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', '', '', 'nba')


async def setup(client: commands.Bot):
    await client.add_cog(nba_live_stream(client))
