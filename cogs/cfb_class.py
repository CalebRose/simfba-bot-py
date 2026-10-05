import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class cfb_class(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cfb_class", description="Look up a college football teams crooting class")
    async def cfb_class(self, interaction: discord.Interaction, team: str):
        upper_input = team.upper()
        team_id = id_util.GetCollegeFootballTeamID(upper_input)
        logo_url = logos_util.GetCFBLogo(team_id)
        data = api_requests.GetCollegeFootballCrootingClass(team_id)
        team = api_requests.GetCollegeFootballTeam(team_id)
        if data == False:
            await interaction.response.send_message(f"Could not find team: {input}")
        else:
            a = 0
            color = team["TeamData"]
            recruits = data["Recruits"]
            title = f"{data['Team']} Recruiting Class"
            desc = f"**Total Recruits:** {data['TotalCommitments']}"
            embed = discord.Embed(colour=discord.Colour.from_str(color["ColorOne"]),
                                description=desc,
                                title=title)
            embed.add_field(name="", value=f"**Composite Score:** {round(data['CompositeScore'],2)}", inline=False)
            embed.add_field(name="ESPN Score", value=round(data['ESPNScore'],2), inline=True)
            embed.add_field(name="Rivals Score", value=round(data['RivalsScore'],2), inline=True)
            embed.add_field(name="247 Score", value=round(data['Rank247Score'],2), inline=True)
            
            try:
                for i in recruits:
                    if a >= 20:
                        break
                    recruit = recruits[a]["Recruit"]
                    embed.add_field(name=f"{recruit['FirstName']} {recruit['LastName']} {recruit['ID']}", value=f"{recruit['Stars']} Star {recruit['Archetype']} {recruit['Position']} from {recruit['State']}" +
                                    f"\nOverall: {recruit['OverallGrade']} \nPotential: {recruit['PotentialGrade']}", inline=False)
                    
                    a += 1


            except TypeError:
                embed.add_field(name="", value=f"{data['Team']} has not signed any croots", inline=False)

            embed.set_thumbnail(url=logo_url)
            await interaction.response.send_message(embed=embed)
                
async def setup(client: commands.Bot):
    await client.add_cog(cfb_class(client))
