import discord
from discord.ext import commands
from discord import app_commands
from helper import cfb_stream_builder
import settings

channel_id = settings.FCS_STREAM_CHANNEL

class fcs_live_stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    fcs_stream_group = app_commands.Group(name="fcs_streams", description="Stream SimCFB FCS Games")


    @fcs_stream_group.command(name="thursday", description="The timeslot you'd like to stream")
    async def thursday(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FCS Thursday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fcs', 'Thursday Night', False)

    @fcs_stream_group.command(name="friday", description="The timeslot you'd like to stream")
    async def friday(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FCS Friday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fcs', 'Friday Night', False)

    @fcs_stream_group.command(name="saturday_morning", description="The timeslot you'd like to stream")
    async def saturday_morning(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FCS Saturday Morning Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fcs','Saturday Morning', False)

    @fcs_stream_group.command(name="saturday_afternoon", description="The timeslot you'd like to stream")
    async def saturday_afternoon(self, interaction: discord.Integration):
            chan = self.client.get_channel(channel_id)
            await interaction.response.send_message("Loading FCS Saturday Afternoon Games...")
            await cfb_stream_builder.stream_fb_game(chan, 'fcs','Saturday Afternoon', False)

    @fcs_stream_group.command(name="saturday_evening", description="The timeslot you'd like to stream")
    async def saturday_evening(self, interaction: discord.Integration):
            chan = self.client.get_channel(channel_id)
            await interaction.response.send_message("Loading FCS Saturday Evening Games...")
            await cfb_stream_builder.stream_fb_game(chan, 'fcs','Saturday Evening', False)

    @fcs_stream_group.command(name="saturday_night", description="The timeslot you'd like to stream")
    async def saturday_night(self, interaction: discord.Integration):
            chan = self.client.get_channel(channel_id)
            await interaction.response.send_message("Loading Big Sky After Dark...")
            await cfb_stream_builder.stream_fb_game(chan, 'fcs','Saturday Night', False)

async def setup(client: commands.Bot):
    await client.add_cog(fcs_live_stream(client))