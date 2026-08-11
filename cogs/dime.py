import discord
from discord.ext import commands
from discord import app_commands

class dime(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="dime", description="Want to place a dime in the jar?")
    async def when(self, interaction: discord.Interaction):
        message = "A dime has been placed into the jar."
        await interaction.response.send_message(message)

async def setup(client: commands.Bot):
    await client.add_cog(dime(client))