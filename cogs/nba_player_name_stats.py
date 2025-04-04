import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class nba_player_name_stats(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="nba_player_name_stats", description="Look up a profesional basketball player using a {first name}, {last name}, and {team}")
    async def nfl_player_name_stats(self, interaction: discord.Interaction, first_name: str, last_name: str, team: str):
        team_abbreviation = team.upper()
        try:
            team_id = id_util.GetNBATeamID(team_abbreviation)
            logo_url = logos_util.GetNBALogo(team_id)
            data = api_requests.GetNBABasketballPlayer(first_name, last_name, team_id)
            if data == False:
                await interaction.response.send_message(f"Could not find player")
            else:
                stats = data["SeasonStats"]
                title = f"{data['FirstName']} {data['LastName']} {data['Position']}"
                desc = f"{data['Year']} year veteran {data['Archetype']} {data['Position']} Graduated from {data['College']}"
                embed = discord.Embed(colour=discord.Colour.orange(),
                                    description=desc,
                                    title=title)

                # Player Stats Embeds
                embed.add_field(name="Games Played", value=stats['GamesPlayed'], inline=True)
                embed.add_field(name="Minutes Per Game", value=stats['MinutesPerGame'], inline=True)
                embed.add_field(name="Possessions Per Game", value=stats['PossessionsPerGame'], inline=True)
                embed.add_field(name="FGs Attempted", value=stats['FGA'], inline=True)
                embed.add_field(name="FGs Made", value=stats['FGM'], inline=True)
                try:
                    embed.add_field(name="FG %", value=str(round((stats['FGM']/stats['FGA'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="FG %", value="N/A", inline=True)
                embed.add_field(name="3 Pointers Attempted", value=stats['ThreePointAttempts'], inline=True)
                embed.add_field(name="3 Pointers Made", value=stats['ThreePointsMade'], inline=True)
                try:
                    embed.add_field(name="3 Point %", value=str(round((stats['ThreePointsMade']/stats['ThreePointAttempts'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="3 Point %", value="N/A", inline=True)
                embed.add_field(name="FTs Attempted", value=stats['FTA'], inline=True)
                embed.add_field(name="FTs Made", value=stats['FTM'], inline=True)
                try:
                    embed.add_field(name="FT %", value=str(round((stats['FTM']/stats['FTA'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="FT %", value="N/A", inline=True)
                embed.add_field(name="Offensive Rebounds", value=stats['OffRebounds'], inline=True)
                embed.add_field(name="Defensiv Rebounds", value=stats['DefRebounds'], inline=True)
                embed.add_field(name="Total Rebounds", value=stats['TotalRebounds'], inline=True)
                embed.add_field(name="Assists", value=stats['Assists'], inline=True)
                embed.add_field(name="Steals", value=stats['Steals'], inline=True)
                embed.add_field(name="Blocks", value=stats['Blocks'], inline=True)
                embed.add_field(name="Turnovers", value=stats['Turnovers'], inline=True)
                embed.add_field(name="Fouls", value=stats['Fouls'], inline=True)
                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(nba_player_name_stats(client))
