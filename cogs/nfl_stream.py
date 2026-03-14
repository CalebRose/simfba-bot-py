import discord
from discord.ext import commands
from discord import app_commands
from helper import cfb_stream_builder
import settings

channel_id = settings.NFL_STREAM_CHANNEL

class NFL_Live_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    nfl_stream_group = app_commands.Group(name="nfl_streams", description="Stream SimNFL Games")


    @nfl_stream_group.command(name="thursday_night", description="The timeslot you'd like to stream")
    async def thursday_night(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Thursday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Thursday Night Football', True)

    @nfl_stream_group.command(name="sunday_noon", description="The timeslot you'd like to stream")
    async def sunday_noon(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Sunday Noon Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Sunday Noon', True)

    @nfl_stream_group.command(name="sunday_afternoon", description="The timeslot you'd like to stream")
    async def sunday_afternoon(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Sunday Afternoon Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Sunday Afternoon', True)

    @nfl_stream_group.command(name="sunday_night", description="The timeslot you'd like to stream")
    async def sunday_night(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Sunday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Sunday Night Football', True)

    @nfl_stream_group.command(name="monday_night", description="The timeslot you'd like to stream")
    async def monday_night(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Monday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Monday Night Football', True)

async def setup(client: commands.Bot):
    await client.add_cog(NFL_Live_Stream(client))