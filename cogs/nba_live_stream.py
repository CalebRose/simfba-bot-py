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

    @nba_stream_group.command(name="int_a", description="The timeslot you'd like to stream")
    async def int_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimNBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', '', 'a', 'nba')

    @nba_stream_group.command(name="int_b", description="The timeslot you'd like to stream")
    async def int_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimNBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', '', 'b', 'nba')

    @nba_stream_group.command(name="int_c", description="The timeslot you'd like to stream")
    async def int_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimNBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', '', 'c', 'nba')

    @nba_stream_group.command(name="int_d", description="The timeslot you'd like to stream")
    async def int_d(self, interaction: discord.Integration):
        chan = self.client.get_channel(int_channel_id)
        await interaction.response.send_message("Loading SimNBA International Games...")
        await nba_stream_builder.stream_game(chan, 'int', '', 'd', 'nba')

    @nba_stream_group.command(name="nbatv_a", description="The timeslot you'd like to stream")
    async def nbatv_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimNBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', '', 'a', 'nba')

    @nba_stream_group.command(name="nbatv_b", description="The timeslot you'd like to stream")
    async def nbatv_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimNBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', '', 'b', 'nba')

    @nba_stream_group.command(name="nbatv_c", description="The timeslot you'd like to stream")
    async def nbatv_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimNBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', '', 'c', 'nba')

    @nba_stream_group.command(name="nbatv_d", description="The timeslot you'd like to stream")
    async def nbatv_d(self, interaction: discord.Integration):
        chan = self.client.get_channel(nbatv_channel_id)
        await interaction.response.send_message("Loading SimNBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', '', 'd', 'nba')

    @nba_stream_group.command(name="tnt_a", description="The timeslot you'd like to stream")
    async def tnt_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimNBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', '', 'a', 'nba')

    @nba_stream_group.command(name="tnt_b", description="The timeslot you'd like to stream")
    async def tnt_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimNBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', '', 'b', 'nba')

    @nba_stream_group.command(name="tnt_c", description="The timeslot you'd like to stream")
    async def tnt_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimNBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', '', 'c', 'nba')

    @nba_stream_group.command(name="tnt_d", description="The timeslot you'd like to stream")
    async def tnt_d(self, interaction: discord.Integration):
        chan = self.client.get_channel(tnt_channel_id)
        await interaction.response.send_message("Loading SimNBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', '', 'd', 'nba')

    @nba_stream_group.command(name="prime_a", description="The timeslot you'd like to stream")
    async def prime_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(nba_prime_channel_id)
        await interaction.response.send_message("Loading SimNBA Prime Time Games...")
        await nba_stream_builder.stream_game(chan, 'prime', '', 'a', 'nba')

    @nba_stream_group.command(name="prime_b", description="The timeslot you'd like to stream")
    async def prime_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(nba_prime_channel_id)
        await interaction.response.send_message("Loading SimNBA Prime Time Games...")
        await nba_stream_builder.stream_game(chan, 'prime', '', 'b', 'nba')

    @nba_stream_group.command(name="prime_c", description="The timeslot you'd like to stream")
    async def prime_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(nba_prime_channel_id)
        await interaction.response.send_message("Loading SimNBA Prime Time Games...")
        await nba_stream_builder.stream_game(chan, 'prime', '', 'c', 'nba')

    @nba_stream_group.command(name="prime_d", description="The timeslot you'd like to stream")
    async def prime_d(self, interaction: discord.Integration):
        chan = self.client.get_channel(nba_prime_channel_id)
        await interaction.response.send_message("Loading SimNBA Prime Time Games...")
        await nba_stream_builder.stream_game(chan, 'prime', '', 'd', 'nba')

    @nba_stream_group.command(name="hbo_a", description="The timeslot you'd like to stream")
    async def hbo_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(nba_hbo_channel_id)
        await interaction.response.send_message("Loading SimNBA HBO Games...")
        await nba_stream_builder.stream_game(chan, 'hbo', '', 'a', 'nba')

    @nba_stream_group.command(name="hbo_b", description="The timeslot you'd like to stream")
    async def hbo_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(nba_hbo_channel_id)
        await interaction.response.send_message("Loading SimNBA HBO Games...")
        await nba_stream_builder.stream_game(chan, 'hbo', '', 'b', 'nba')

    @nba_stream_group.command(name="hbo_c", description="The timeslot you'd like to stream")
    async def hbo_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(nba_hbo_channel_id)
        await interaction.response.send_message("Loading SimNBA HBO Games...")
        await nba_stream_builder.stream_game(chan, 'hbo', '', 'c', 'nba')

    @nba_stream_group.command(name="hbo_d", description="The timeslot you'd like to stream")
    async def hbo_d(self, interaction: discord.Integration):
        chan = self.client.get_channel(nba_hbo_channel_id)
        await interaction.response.send_message("Loading SimNBA HBO Games...")
        await nba_stream_builder.stream_game(chan, 'hbo', '', 'd', 'nba')


async def setup(client: commands.Bot):
    await client.add_cog(nba_live_stream(client))