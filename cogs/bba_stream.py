import discord
from discord.ext import commands
from discord import app_commands
from helper import cbb_stream_builder
import settings

cbb_channel_id = settings.CBB_STREAM_CHANNEL
tbs_channel_id = settings.TBS_STREAM_CHANNEL
espn_channel_id = settings.ESPN_STREAM_CHANNEL
espn2_channel_id = settings.ESPN2_STREAM_CHANNEL

class bba_stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    cbb_stream_group = app_commands.Group(name="bba_streams", description="Stream SimCBB Games")

    @cbb_stream_group.command(name="cbb", description="Stream the CBS games")
    async def cbb(self, interaction: discord.Interaction):
        chan = self.client.get_channel(cbb_channel_id)
        await interaction.response.send_message("Loading SimBBA CBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'cbs', '', '', '')

    @cbb_stream_group.command(name="espn", description="Stream the ESPN games")
    async def espn(self, interaction: discord.Interaction):
        chan = self.client.get_channel(espn_channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn', '', '', '')

    @cbb_stream_group.command(name="ytv", description="Stream the YTV games")
    async def ytv(self, interaction: discord.Interaction):
        chan = self.client.get_channel(espn2_channel_id)
        await interaction.response.send_message("Loading SimBBA YTV Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'ytv', '', '', '')

    @cbb_stream_group.command(name="tbs", description="Stream the TBS games")
    async def tbs(self, interaction: discord.Interaction):
        chan = self.client.get_channel(tbs_channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', '', '', '')


async def setup(client: commands.Bot):
    await client.add_cog(bba_stream(client))
