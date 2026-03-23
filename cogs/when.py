import discord
from discord.ext import commands
from discord import app_commands

class when(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="when", description="An FAQ for the most common questions asked in Discord.")
    async def when(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="An FAQ for the most common questions asked in Discord.",
                            title="When...")
        embed.add_field(name="does recruiting run in SimCFB?", value="Between weeks 1 through 20 in the regular season, every Wednesday sometime around Noon EST.", inline=False)
        embed.add_field(name="does recruiting run in SimCBB?", value="Between weeks 1 through 15 in the regular season, every Wednesday sometime around Noon EST.", inline=False)
        embed.add_field(name="does recruiting run in SimCHL?", value="Between weeks 1 through 20 in the regular season, every Wednesday sometime around Noon EST.", inline=False)
        embed.add_field(name="does Free Agency run in our pro leagues?", value="Every day at around Noon EST.", inline=False)
        embed.add_field(name="do minimum values decrease for SimNFL FA Veterans?", value="FA minimum values gradually decreases down to 70% value, after the SimNFL Draft takes place.", inline=False)
        embed.add_field(name="do the college polls run in SimCFB?", value="After the Monday Weekly Sync.", inline=False)
        embed.add_field(name="do the college polls run in SimCBB?", value="Every Sunday Morning.", inline=False)
        embed.add_field(name="do the college polls run in SimCHL?", value="Every Sunday Afternoon.", inline=False)
        embed.add_field(name="do football games run?", value="Wednesdays by Midnight. Have your gameplans & depth charts ready by then.", inline=False)
        embed.add_field(name="do basketball games run?", value="Monday, Wednesday, Friday, and Saturday Mornings. Have your gameplans ready by then.", inline=False)
        embed.add_field(name="do hockey games run?", value="Tuesdays, Thursdays, Saturdays, and Sundays. Have your gameplans ready by then.", inline=False)
        embed.add_field(name="do baseball games run?", value="I don't know, ask Alexfall about that.", inline=False)
        embed.add_field(name="will Guam join the FCS?", value="Soon.", inline=False)


        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(when(client))
