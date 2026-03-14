import discord
from discord.ext import commands
from discord import app_commands
from helper import cfb_stream_builder
import settings

channel_id = settings.STREAM_CHANNEL
big_noon_id = settings.B1G_NOON
after_dark_id = settings.AFTER_DARK
prime_time = settings.PRIME_TIME

class cfb_live_stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    fbs_stream_group = app_commands.Group(name="fbs_streams", description="Stream SimCFB FBS Games")

    @fbs_stream_group.command(name="thursday", description="The timeslot you'd like to stream")
    async def thursday(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FBS Thursday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fbs', 'Thursday Night', False)

    @fbs_stream_group.command(name="friday", description="The timeslot you'd like to stream")
    async def friday(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FBS Friday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fbs', 'Friday Night', False)

    @fbs_stream_group.command(name="saturday_morning", description="The timeslot you'd like to stream")
    async def saturday_morning(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FBS Saturday Morning Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fbs','Saturday Morning', False)

    @fbs_stream_group.command(name="saturday_afternoon", description="The timeslot you'd like to stream")
    async def saturday_afternoon(self, interaction: discord.Integration):
            chan = self.client.get_channel(big_noon_id)
            await interaction.response.send_message("Loading FBS Saturday Afternoon Games...")
            await cfb_stream_builder.stream_fb_game(chan, 'fbs','Saturday Afternoon', False)

    @fbs_stream_group.command(name="saturday_evening", description="The timeslot you'd like to stream")
    async def saturday_evening(self, interaction: discord.Integration):
            chan = self.client.get_channel(prime_time)
            await interaction.response.send_message("Loading FBS Saturday Evening Games...")
            await cfb_stream_builder.stream_fb_game(chan, 'fbs','Saturday Evening', False)

    @fbs_stream_group.command(name="saturday_night", description="The timeslot you'd like to stream")
    async def saturday_night(self, interaction: discord.Integration):
            chan = self.client.get_channel(after_dark_id)
            await interaction.response.send_message("Loading Pac-2 After Dark...")
            await cfb_stream_builder.stream_fb_game(chan, 'fbs','Saturday Night', False)

async def setup(client: commands.Bot):
    await client.add_cog(cfb_live_stream(client))