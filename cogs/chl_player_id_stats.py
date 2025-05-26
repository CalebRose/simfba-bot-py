import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class chl_player_id_stats(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="chl_player_id_stats", description="Look up a college hockey player using a player {id}")
    async def chl_player_id_stats(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetCollegeHockeyPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                stats = data["CollegeStats"]
                year = data["Year"]
                open = ""
                close = ""
                if data["IsRedshirt"] == True:
                    year = year-1
                    open = "("
                    close = ")"
                if year == 1:
                    year = "Fr"
                elif year == 2:
                    year = "So"
                elif year == 3:
                    year = "Jr"
                elif year == 4:
                    year = "Sr"
                title = f"{data['FirstName']} {data['LastName']} {data['Position']} {data['PlayerID']}"
                if {data['City']} == {data['State']}:
                    desc = f"{data['Stars']} Star {open}{year}{close} {data['Archetype']} {data['Position']} from {data['City']}, {data['Country']}"
                else:
                    desc = f"{data['Stars']} Star {open}{year}{close} {data['Archetype']} {data['Position']} from {data['City']}, {data['State']}, {data['Country']}"
                team_id = id_util.GetCollegeHockeyTeamID(data['Team'].upper())
                logo_url = logos_util.GetCHLLogo(team_id)
                embed = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)

                if stats["GamesPlayed"] > 0:
                    embed.add_field(name="Games Played", value=stats["GamesPlayed"])
                    if data["Position"] == "G":
                        embed.add_field(name="", value="")
                        embed.add_field(name="", value="")
                        embed.add_field(name="Wins", value=stats["GoalieWins"])
                        embed.add_field(name="Losses", value=stats["GoalieLosses"])
                        embed.add_field(name="Ties", value=stats["GoalieTies"])
                        embed.add_field(name="Overtime Losses", value=stats["OvertimeLosses"])
                        embed.add_field(name="Shots Against", value=stats["ShotsAgainst"])
                        embed.add_field(name="Saves", value=stats["Saves"])
                        embed.add_field(name="Goals Allowed", value=stats["GoalsAgainst"])
                        embed.add_field(name="Save Percentage", value=stats["SavePercentage"])
                        gaa = stats["GoalsAgainst"]/stats["GamesPlayed"]
                        embed.add_field(name="Goals Against Average", value=gaa)
                        embed.add_field(name="Shutouts", value=stats["Shutouts"])
                        if stats["Goals"] > 0:
                            embed.add_field(name="Goals", value=stats["Goals"])
                        if stats["Assists"] > 0:
                            embed.add_field(name="Assists", value=stats["Assists"])
                    else:
                        embed.add_field(name="", value="")
                        embed.add_field(name="Time on Ice", value=stats["TimeOnIce"])
                        if data["Position"] == "C":
                             embed.add_field(name="Faceoffs Taken", value=stats["FaceOffs"])
                             embed.add_field(name="Faceoffs Won", value=stats["FaceOffsWon"])
                             embed.add_field(name="Faceoff Percentage", value=stats["FaceOffWinPercentage"])
                        embed.add_field(name="Goals", value=stats["Goals"])
                        embed.add_field(name="Assists", value=stats["Assists"])
                        embed.add_field(name="Points", value=stats["Points"])
                        if stats["Points"] > stats["EvenStrengthPoints"]:
                            embed.add_field(name="Even Strength Goals", value=stats["EvenStrengthGoals"])
                            eassist = stats["EvenStrengthPoints"]-stats["EvenStrengthGoals"]
                            embed.add_field(name="Even Strength Assists", value=eassist)
                            if stats["PowerPlayPoints"] > 0:
                                embed.add_field(name="Power Play Goals", value=stats["PowerPlayGoals"])
                                passist = stats["PowerPlayPoints"]-stats["PowerPlayGoals"]
                                embed.add_field(name="Power Play Assists", value=passist)
                            if stats["ShorthandedPoints"] > 0:
                                embed.add_field(name="Shorthanded Goals", value=stats["ShorthandedGoals"])
                                sassist = stats["ShorthandedPoints"]-stats["ShorthandedGoals"]
                                embed.add_field(name="Shorthanded Assists", value=sassist)
                        embed.add_field(name="Overtime Goals", value=stats["OvertimeGoals"])
                        embed.add_field(name="Game Winning Goals", value=stats["GameWinningGoals"])
                        embed.add_field(name="Plus/Minus", value=stats["PlusMinus"])
                        embed.add_field(name="Shots", value=stats["Shots"])
                        embed.add_field(name="Shooting Percentage", value=stats["ShootingPercentage"])
                        embed.add_field(name="Shots Blocked", value=stats["ShotsBlocked"])
                        embed.add_field(name="Body Checks", value=stats["BodyChecks"])
                        embed.add_field(name="Stick Checks", value=stats["StickChecks"])
                        embed.add_field(name="PenaltyMinutes", value=stats["PenaltyMinutes"])
                else:
                        embed.add_field(name="",value="Stats work best on players who have actually played games")

                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(chl_player_id_stats(client))
