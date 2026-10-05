import discord
from discord.ext import commands
from discord import app_commands
from helper import nba_stream_builder
import settings

nbatv_channel_id = settings.NBA_LIVE_STREAM_CHANNEL
tnt_channel_id = settings.TNT_STREAM_CHANNEL
int_channel_id = settings.INT_STREAM_CHANNEL

class nba_live_stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    nba_stream_group = app_commands.Group(name="nba_streams", description="Stream SimNBA Basketball Games")

    @nba_stream_group.command(name="int_a", description="The timeslot you'd like to stream")
    async def int_a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimBBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', input, 'a', 'nba')

    @nba_stream_group.command(name="int_b", description="The timeslot you'd like to stream")
    async def int_b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimBBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', input, 'b', 'nba')

    @nba_stream_group.command(name="int_c", description="The timeslot you'd like to stream")
    async def int_c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimBBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', input, 'c', 'nba')

    @nba_stream_group.command(name="int_d", description="The timeslot you'd like to stream")
    async def int_d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimBBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', input, 'd', 'nba')

    @nba_stream_group.command(name="nbatv_a", description="The timeslot you'd like to stream")
    async def nbatv_a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimBBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', input, 'a', 'nba')

    @nba_stream_group.command(name="nbatv_b", description="The timeslot you'd like to stream")
    async def nbatv_b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimBBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', input, 'b', 'nba')

    @nba_stream_group.command(name="nbatv_c", description="The timeslot you'd like to stream")
    async def nbatv_c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimBBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', input, 'c', 'nba')

    @nba_stream_group.command(name="nbatv_d", description="The timeslot you'd like to stream")
    async def nbatv_d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimBBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', input, 'd', 'nba')

    @nba_stream_group.command(name="tnt_a", description="The timeslot you'd like to stream")
    async def tnt_a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimBBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', input, 'a', 'nba')

    @nba_stream_group.command(name="tnt_b", description="The timeslot you'd like to stream")
    async def tnt_b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimBBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', input, 'b', 'nba')

    @nba_stream_group.command(name="tnt_c", description="The timeslot you'd like to stream")
    async def tnt_c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimBBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', input, 'c', 'nba')

    @nba_stream_group.command(name="tnt_d", description="The timeslot you'd like to stream")
    async def tnt_d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimBBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', input, 'd', 'nba')

async def setup(client: commands.Bot):
    await client.add_cog(nba_live_stream(client))