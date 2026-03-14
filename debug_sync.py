import discord
from discord.ext import commands
import asyncio
import settings
import sys
import platform

class DebugBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        print(f"🔍 DIAGNOSTIC INFO:")
        print(f"   Platform: {platform.platform()}")
        print(f"   Python: {sys.version}")
        print(f"   Discord.py: {discord.__version__}")
        print(f"   Bot User: {self.user}")
        print(f"   Guild ID: {settings.GUILDS_ID}")
        print()
        
        print("📊 CHECKING PERMISSIONS...")
        try:
            guild = self.get_guild(settings.GUILDS_ID.id if hasattr(settings.GUILDS_ID, 'id') else settings.GUILDS_ID)
            if guild:
                print(f"   ✅ Connected to guild: {guild.name}")
                me = guild.get_member(self.user.id)
                if me:
                    print(f"   ✅ Bot is member of guild")
                    print(f"   Permissions: {me.guild_permissions}")
                    print(f"   Can use slash commands: {me.guild_permissions.use_slash_commands}")
                    print(f"   Is administrator: {me.guild_permissions.administrator}")
                else:
                    print(f"   ❌ Bot is not a member of the guild")
            else:
                print(f"   ❌ Cannot access guild with ID: {settings.GUILDS_ID}")
        except Exception as e:
            print(f"   ❌ Error checking guild: {e}")
        
        print()
        print("🔄 ATTEMPTING COMMAND SYNC...")
        
        try:
            # Try global sync first
            print("   Syncing global commands...")
            synced_global = await self.tree.sync()
            print(f"   ✅ Global sync successful: {len(synced_global)} commands")
            
            # Try guild sync
            print(f"   Syncing guild commands for {settings.GUILDS_ID}...")
            synced_guild = await self.tree.sync(guild=settings.GUILDS_ID)
            print(f"   ✅ Guild sync successful: {len(synced_guild)} commands")
            
        except discord.Forbidden as e:
            print(f"   ❌ FORBIDDEN ERROR: {e}")
            print("   This usually means the bot lacks permissions or isn't properly invited")
        except discord.HTTPException as e:
            print(f"   ❌ HTTP ERROR: {e}")
            print("   This could be rate limiting or network issues")
        except Exception as e:
            print(f"   ❌ UNKNOWN ERROR: {e}")
            print(f"   Error type: {type(e)}")
        
        print()
        print("🏁 DIAGNOSTIC COMPLETE")
        print("Closing bot...")
        await self.close()

    async def on_ready(self):
        print(f'✅ Logged in as {self.user} (ID: {self.user.id})')

async def main():
    bot = DebugBot()
    try:
        await bot.start(settings.DISCORD_API_SECRET)
    except Exception as e:
        print(f"❌ Failed to start bot: {e}")

if __name__ == "__main__":
    print("🔧 Discord Bot Sync Diagnostics")
    print("=" * 40)
    asyncio.run(main())