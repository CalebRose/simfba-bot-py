import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests

class cbb_croot(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cbb_croot", description="Look up a croot using a croot {id}")
    async def cbb_croot(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetCollegeBasketballCroot(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:

                title = f" {id} {data[0]['FirstName']} {data[0]['LastName']}"
                desc = f"{data[0]['Stars']} Star {data[0]['Position']} from {data[0]['State']}, {data[0]['Country']}"
                team_id = id_util.GetCollegeBasketballTeamID(data[0]["College"].upper())
                logo_url = logos_util.GetCBBLogo(team_id)
                team = api_requests.GetCollegeBasketballTeam(team_id)
                if team_id != "/":
                    color = team["TeamData"]
                    embed = discord.Embed(colour=discord.Colour.from_str(color["ColorOne"]),
                                    description=desc,
                                    title=title)
                else:
                    embed = discord.Embed(colour=discord.Colour.dark_gold(),
                                    description=desc,
                                    title=title)
                if len(data[0]["SigningStatus"]) > 0:
                    embed.add_field(name="Recruiting Status", value=data[0]["SigningStatus"], inline=False)
                embed.add_field(name="Personality", value=data[0]["Personality"], inline=True)
                embed.add_field(name="Recruiting Bias", value=data[0]["RecruitingBias"], inline=True)
                embed.add_field(name="Academic Bias", value=data[0]["AcademicBias"], inline=True)
                embed.add_field(name="Work Ethic", value=data[0]["WorkEthic"], inline=True)

                try:
                    embed.add_field(name="Leading Teams", value="", inline=False)
                    leading_teams = data[0]["LeadingTeams"]
                    a = 0

                    if data[0]['IsSigned'] == True:
                        for i in leading_teams:
                            if leading_teams[a]["Odds"] > 0:
                                embed.add_field(name=leading_teams[a]["TeamAbbr"], value=f"Odds {round(leading_teams[a]['Odds']*100,2)}%", inline=True)
                            a += 1
                    else:
                        for i in leading_teams:
                            if leading_teams[a]["Odds"] > 0:
                               odds = round(leading_teams[a]["Odds"]*100,2)
                               if odds > 45:
                                   embed.add_field(name=leading_teams[a]["TeamAbbr"], value="Strong Favorite", inline=True)
                               elif odds > 24:
                                   embed.add_field(name=leading_teams[a]["TeamAbbr"], value="In Contention", inline=True)
                               elif odds > 11:
                                   embed.add_field(name=leading_teams[a]["TeamAbbr"], value="Just Outside", inline=True)
                               else:
                                   embed.add_field(name=leading_teams[a]["TeamAbbr"], value="Unlikely", inline=True)
                            a += 1
                            
                except TypeError:
                    embed.add_field(name="", value=f"{data[0]['FirstName']} {data[0]['LastName']} has no leading teams", inline=False)

                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="Simulation Sports Network")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(cbb_croot(client))
