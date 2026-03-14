import discord
from discord.ext import commands
from discord import app_commands
from helper import hockey_stream_builder
import settings
import asyncio


tsn_id = settings.TSN_STREAM_CHANNEL
polar_id = settings.POLAR_STREAM_CHANNEL
frozen_id = settings.FROZEN_STREAM_CHANNEL

class PHL_Hockey_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    phl_stream_group = app_commands.Group(name="phl_streams", description="Stream SimPHL Games")
    @phl_stream_group.command(name="tsn_a", description="The timeslot you'd like to stream")
    async def tsn_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(tsn_id)
        await interaction.response.send_message("Loading HCK_Live games for Game A...")
        await hockey_stream_builder.stream_hockey_game(chan, '1', 'phl')
    @phl_stream_group.command(name="tsn_b", description="The timeslot you'd like to stream")
    async def tsn_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(tsn_id)
        await interaction.response.send_message("Loading HCK_Live games for Game B...")
        await hockey_stream_builder.stream_hockey_game(chan, '1', 'phl')
    @phl_stream_group.command(name="tsn_c", description="The timeslot you'd like to stream")
    async def tsn_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(tsn_id)
        await interaction.response.send_message("Loading HCK_Live games for Game C...")
        await hockey_stream_builder.stream_hockey_game(chan, '1', 'phl')
    @phl_stream_group.command(name="tsn_d", description="The timeslot you'd like to stream")
    async def tsn_d(self, interaction: discord.Integration):
        chan = self.client.get_channel(tsn_id)
        await interaction.response.send_message("Loading HCK_Live games for Game D...")
        await hockey_stream_builder.stream_hockey_game(chan, '1', 'phl')

    @phl_stream_group.command(name="polar_a", description="The timeslot you'd like to stream")
    async def polar_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(polar_id)
        await interaction.response.send_message("Loading HCK_Live games for Game A...")
        await hockey_stream_builder.stream_hockey_game(chan, '2', 'phl')
    @phl_stream_group.command(name="polar_b", description="The timeslot you'd like to stream")
    async def polar_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(polar_id)
        await interaction.response.send_message("Loading HCK_Live games for Game B...")
        await hockey_stream_builder.stream_hockey_game(chan, '2', 'phl')
    @phl_stream_group.command(name="polar_c", description="The timeslot you'd like to stream")
    async def polar_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(polar_id)
        await interaction.response.send_message("Loading HCK_Live games for Game C...")
        await hockey_stream_builder.stream_hockey_game(chan, '2', 'phl')
    @phl_stream_group.command(name="polar_d", description="The timeslot you'd like to stream")
    async def polar_d(self, interaction: discord.Integration):
        chan = self.client.get_channel(polar_id)
        await interaction.response.send_message("Loading HCK_Live games for Game D...")
        await hockey_stream_builder.stream_hockey_game(chan, '2', 'phl')        

    @phl_stream_group.command(name="frozen_a", description="The timeslot you'd like to stream")
    async def frozen_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(frozen_id)
        await interaction.response.send_message("Loading HCK_Live games for Game A...")
        await hockey_stream_builder.stream_hockey_game(chan, '3', 'phl')
    @phl_stream_group.command(name="frozen_b", description="The timeslot you'd like to stream")
    async def frozen_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(frozen_id)
        await interaction.response.send_message("Loading HCK_Live games for Game B...")
        await hockey_stream_builder.stream_hockey_game(chan, '3', 'phl')
    @phl_stream_group.command(name="frozen_c", description="The timeslot you'd like to stream")
    async def frozen_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(frozen_id)
        await interaction.response.send_message("Loading HCK_Live games for Game C...")
        await hockey_stream_builder.stream_hockey_game(chan, '3', 'phl')
    @phl_stream_group.command(name="frozen_d", description="The timeslot you'd like to stream")
    async def frozen_d(self, interaction: discord.Integration):
        chan = self.client.get_channel(frozen_id)
        await interaction.response.send_message("Loading HCK_Live games for Game D...")
        await hockey_stream_builder.stream_hockey_game(chan, '3', 'phl')


async def setup(client: commands.Bot):
    await client.add_cog(PHL_Hockey_Stream(client))