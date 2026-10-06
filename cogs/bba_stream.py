import discord
from discord.ext import commands
from discord import app_commands
from helper import cbb_stream_builder
from helper import nba_stream_builder
import settings

cbb_channel_id = settings.CBB_STREAM_CHANNEL
tbs_channel_id = settings.TBS_STREAM_CHANNEL
espn_channel_id = settings.ESPN_STREAM_CHANNEL
espn2_channel_id = settings.ESPN2_STREAM_CHANNEL

class bba_stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    cbb_stream_group = app_commands.Group(name="bba_streams", description="Stream SimCBB Games")


    @cbb_stream_group.command(name="cbb_a", description="The timeslot you'd like to stream")
    async def cbb_a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(cbb_channel_id)
        await interaction.response.send_message("Loading SimBBA CBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'cbs', input, 'a', '')

    @cbb_stream_group.command(name="cbb_b", description="The timeslot you'd like to stream")
    async def cbb_b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(cbb_channel_id)
        await interaction.response.send_message("Loading SimBBA CBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'cbs', input, 'b', '')

    @cbb_stream_group.command(name="cbb_c", description="The timeslot you'd like to stream")
    async def cbb_c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(cbb_channel_id)
        await interaction.response.send_message("Loading SimBBA CBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'cbs', input, 'c', '')

    @cbb_stream_group.command(name="cbb_d", description="The timeslot you'd like to stream")
    async def cbb_d(self, interaction: discord.Integration, input: str):
            chan = self.client.get_channel(cbb_channel_id)
            await interaction.response.send_message("Loading SimBBA CBS Games...")
            await cbb_stream_builder.stream_cbb_game(chan, 'cbs', input, 'd', '')


    @cbb_stream_group.command(name="espn_a", description="The timeslot you'd like to stream")
    async def espn_a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(espn_channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn', input, 'a', '')

    @cbb_stream_group.command(name="espn_b", description="The timeslot you'd like to stream")
    async def espn_b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(espn_channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn', input, 'b', '')

    @cbb_stream_group.command(name="espn_c", description="The timeslot you'd like to stream")
    async def espn_c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(espn_channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn', input, 'c', '')

    @cbb_stream_group.command(name="espn_d", description="The timeslot you'd like to stream")
    async def espn_d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(espn_channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn', input, 'd', '')

    @cbb_stream_group.command(name="ytv_a", description="The timeslot you'd like to stream")
    async def espn2_a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(espn2_channel_id)
        await interaction.response.send_message("Loading SimBBA YTV Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'ytv', input, 'a', '')

    @cbb_stream_group.command(name="ytv_b", description="The timeslot you'd like to stream")
    async def espn2_b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(espn2_channel_id)
        await interaction.response.send_message("Loading SimBBA YTV Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'ytv', input, 'b', ''  )

    @cbb_stream_group.command(name="ytv_c", description="The timeslot you'd like to stream")
    async def espn2_c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(espn2_channel_id)
        await interaction.response.send_message("Loading SimBBA YTV Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'ytv', input, 'c', '')

    @cbb_stream_group.command(name="ytv_d", description="The timeslot you'd like to stream")
    async def espn2_d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(espn2_channel_id)
        await interaction.response.send_message("Loading SimBBA YTV Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'ytv', input, 'd', '')

    @cbb_stream_group.command(name="tbs_a", description="The timeslot you'd like to stream")
    async def tbs_a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(tbs_channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', input, 'a', '')

    @cbb_stream_group.command(name="tbs_b", description="The timeslot you'd like to stream")
    async def tbs_b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(tbs_channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', input, 'b', '')

    @cbb_stream_group.command(name="tbs_c", description="The timeslot you'd like to stream")
    async def tbs_c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(tbs_channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', input, 'c', '')

    @cbb_stream_group.command(name="tbs_d", description="The timeslot you'd like to stream")
    async def tbs_d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(tbs_channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', input, 'd', '')


async def setup(client: commands.Bot):
    await client.add_cog(bba_stream(client))