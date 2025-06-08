import discord
from discord.ext import commands
from discord import app_commands
from helper import hockey_stream_builder
import settings


channel_id = settings.RINK_STREAM_CHANNEL
cbc_channel_id = settings.CBC_STREAM_CHANNEL
college_u_id = settings.COLLEGE_U_STREAM_CHANNEL

class CHL_Hockey_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        client.tree.add_command(self.chl_stream_group, guild=settings.GUILDS_ID)
    
    chl_stream_group = app_commands.Group(name="chl_streams", description="Stream SimCHL Games")
    @chl_stream_group.command(name="hck_a", description="The timeslot you'd like to stream")
    async def hck_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await chan.send("Loading HCK_Live games for Game A. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '1', '')
    @chl_stream_group.command(name="hck_b", description="The timeslot you'd like to stream")
    async def hck_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await chan.send("Loading HCK_Live games for Game B. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '1', '')
    @chl_stream_group.command(name="hck_c", description="The timeslot you'd like to stream")
    async def hck_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(channel_id)
        await chan.send("Loading HCK_Live games for Game C. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '1', '')

    @chl_stream_group.command(name="cbc_a", description="The timeslot you'd like to stream")
    async def cbc_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(cbc_channel_id)
        await chan.send("Loading HCK_Live games for Game A. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '2', '')
    @chl_stream_group.command(name="cbc_b", description="The timeslot you'd like to stream")
    async def cbc_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(cbc_channel_id)
        await chan.send("Loading HCK_Live games for Game B. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '2', '')
    @chl_stream_group.command(name="cbc_c", description="The timeslot you'd like to stream")
    async def cbc_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(cbc_channel_id)
        await chan.send("Loading HCK_Live games for Game C. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '2', '')

    @chl_stream_group.command(name="college_u_a", description="The timeslot you'd like to stream")
    async def college_u_a(self, interaction: discord.Integration):
        chan = self.client.get_channel(college_u_id)
        await chan.send("Loading HCK_Live games for Game A. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '3', '')
    @chl_stream_group.command(name="college_u_b", description="The timeslot you'd like to stream")
    async def college_u_b(self, interaction: discord.Integration):
        chan = self.client.get_channel(college_u_id)
        await chan.send("Loading HCK_Live games for Game B. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '3', '')
    @chl_stream_group.command(name="college_u_c", description="The timeslot you'd like to stream")
    async def college_u_c(self, interaction: discord.Integration):
        chan = self.client.get_channel(college_u_id)
        await chan.send("Loading HCK_Live games for Game C. All user games take place here.")
        await hockey_stream_builder.stream_hockey_game(chan, '3', '')



async def setup(client: commands.Bot):
    await client.add_cog(CHL_Hockey_Stream(client))