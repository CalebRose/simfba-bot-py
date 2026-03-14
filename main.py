import discord
import os
from discord.ext import commands
from discord import app_commands
from constants import *
import settings

class MyClient(commands.Bot):

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='/', intents=intents)
    async def setup_hook(self):
        print("Starting bot setup...")
        
        print("Loading cogs...")
        list_dir = os.listdir('./cogs')
        for filename in list_dir:
                if filename.endswith('.py'):
                    print(f"Loading {filename[:-3]}...")
                    await self.load_extension(f'cogs.{filename[:-3]}')
        
        print("Syncing commands...")
        # Sync commands globally for all servers where the bot is present
        synced_global = await self.tree.sync()
        print(f'Global Slash CMDs Synced: {len(synced_global)}')
        
        # Also sync to your specific guild for immediate testing
        # self.tree.copy_global_to(guild=settings.GUILDS_ID)
        # synced_guild = await self.tree.sync(guild=settings.GUILDS_ID)
        # print(f'Guild Slash CMDs Synced: {len(synced_guild)}')
        
        print("Bot setup completed!")
        
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_error(self, event, *args, **kwargs):
        print(f"An error occurred in event {event}, args: {args}, kwargs: {kwargs}")

client = MyClient()

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

@client.tree.command()
async def test(interaction: discord.Interaction):
    """Sends the text into the current channel."""
    await interaction.response.send_message("HELLO THERE!")

client.run(settings.DISCORD_API_SECRET, root_logger=True)