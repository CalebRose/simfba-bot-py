import discord
from discord.ext import commands
import asyncio
import settings

class CommandClearer(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        print("Connected to Discord. Clearing commands...")
        
        # Clear global commands
        print("Clearing global commands...")
        self.tree.clear_commands(guild=None)
        synced_global = await self.tree.sync()
        print(f"Global commands cleared. Synced: {len(synced_global)}")
        
        # Clear guild commands
        print(f"Clearing guild commands for guild ID: {settings.GUILDS_ID}...")
        self.tree.clear_commands(guild=settings.GUILDS_ID)
        synced_guild = await self.tree.sync(guild=settings.GUILDS_ID)
        print(f"Guild commands cleared. Synced: {len(synced_guild)}")
        
        print("✅ All commands cleared successfully!")
        print("Closing bot...")
        await self.close()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

async def main():
    bot = CommandClearer()
    try:
        await bot.start(settings.DISCORD_API_SECRET)
    except KeyboardInterrupt:
        print("Bot stopped by user")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Discord Command Clearer")
    print("======================")
    print("This script will clear ALL slash commands from Discord.")
    print("Press Ctrl+C to cancel, or wait 3 seconds to continue...")
    
    try:
        import time
        time.sleep(3)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nCanceled by user")