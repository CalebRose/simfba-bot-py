import discord
import asyncio
from discord.ext import commands
from discord import app_commands
from helper.util import GetYear
import typing
import logos_util
import id_util
import api_requests
import settings

class baseball_player_id(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    baseball_player_id_group = app_commands.Group(name="baseball_player_id", description="Baseball Player by ID")

    @baseball_player_id_group.command(name="batting_stats", description="Look up a players batting stats using an {id} and optional {team abbreviation} and {season}")
    async def batting_stats(self, interaction: discord.Interaction, id: int, team_abbreviation: typing.Optional[str] = None, season: typing.Optional[int] = None):
        try:
            await interaction.response.defer()
            data = api_requests.GetBaseballPlayer_id(id)
            player = api_requests.GetBaseballPlayer_id2(id)
            if data == False:
                await interaction.followup.send(f"Could not find player")
            else:
                batting = data["batting"]
                bio = player["bio"]
                contract = player["contract"]
                vis = player["visibility"]
                seasons = []
                teams = []
                max_season = 0
                if type(season) == int:
                    year_id = season - 2025
                    for index, dictionary in enumerate(batting):
                        if dictionary["league_year_id"] == year_id:
                            seasons.append(index)
                else:
                    for index, dictionary in enumerate(batting):
                        if dictionary["league_year_id"] > max_season:
                            max_season = dictionary["league_year_id"]
                            seasons.clear()
                            seasons.append(index)
                        elif dictionary["league_year_id"] == max_season:
                            seasons.append(index)
                if type(team_abbreviation) == str:
                    teams.clear()
                    team = team_abbreviation.upper()
                    for index, dictionary in enumerate(batting):
                        if dictionary["team_abbrev"] == team:
                            teams.append(index)
                else:
                    for index, dictionary in enumerate(batting):
                        teams.append(index)
                stats_set = set(seasons) & set(teams)
                if not stats_set:
                    await interaction.followup.send(f"Could not find batting stats for that player{' on that team' if type(team_abbreviation) == str else ''}{' for that season' if type(season) == int else ''}")
                else:
                    stats = stats_set.pop()
                    title = f"{data['name']} {player['listed_position']} {id}"
                    if vis['pool'] == "college":
                        redshirt = False
                        if contract['years'] > 4:
                            redshirt = True
                        year = GetYear(contract['current_year'], redshirt)
                        desc = f"{year} from {bio['city']}, {bio['area']}"
                    else:
                        desc = f"{bio['age']} years old from {bio['city']}, {bio['area']}"

                    embed_player = discord.Embed(colour=discord.Colour.gold(),
                                        description=desc,
                                        title=title)
                    embed_player.set_footer(text="Simulation Sports Network")

                    embed_player.add_field(name="Team", value=batting[stats]["team_abbrev"])
                    embed_player.add_field(name="Season", value=f"{batting[stats]['league_year_id']+2025}")
                    embed_player.add_field(name="Games Played", value=batting[stats]["g"])
                    embed_player.add_field(name="Plate Apperances", value=batting[stats]["pa"])
                    embed_player.add_field(name="Batting Average", value=batting[stats]["avg"])
                    embed_player.add_field(name="OBP", value=batting[stats]["obp"])
                    slugging = ((batting[stats]["h"]-batting[stats]["2b"]-batting[stats]["3b"]-batting[stats]["hr"])+(batting[stats]["2b"]*2)+(batting[stats]["3b"]*3)+(batting[stats]["hr"]*4))/batting[stats]["ab"]
                    embed_player.add_field(name="Slugging", value=f"{slugging:.3f}")
                    embed_player.add_field(name="OPS", value=f"{slugging+float(batting[stats]['obp']):.3f}")
                    embed_player.add_field(name="Hits", value=batting[stats]["h"])
                    embed_player.add_field(name="Doubles", value=batting[stats]["2b"])
                    embed_player.add_field(name="Triples", value=batting[stats]["3b"])
                    embed_player.add_field(name="Home Runs", value=batting[stats]["hr"])
                    embed_player.add_field(name="Strike Outs", value=batting[stats]["so"])
                    embed_player.add_field(name="Walks", value=batting[stats]["bb"])
                    embed_player.add_field(name="Runs", value=batting[stats]["r"])
                    embed_player.add_field(name="RBI", value=batting[stats]["rbi"])
                    embed_player.add_field(name="Stolen Bases", value=batting[stats]["sb"])
                    embed_player.add_field(name="Caught Stealing", value=batting[stats]["cs"])

                    await interaction.followup.send(embed=embed_player)
        except Exception as e:
            print(f"Error occured: {e}")

    @baseball_player_id_group.command(name="fielding_stats", description="Look up a players fielding stats using an {id} optional {position} {team abbreviation} and {season}")
    async def fielding_stats(self, interaction: discord.Interaction, id: int, position: typing.Optional[str] = None, team_abbreviation: typing.Optional[str] = None, season: typing.Optional[int] = None):
        try:
            await interaction.response.defer()
            data = api_requests.GetBaseballPlayer_id(id)
            player = api_requests.GetBaseballPlayer_id2(id)
            if data == False:
                await interaction.followup.send(f"Could not find player")
            else:
                fielding = data["fielding"]
                bio = player["bio"]
                contract = player["contract"]
                vis = player["visibility"]
                seasons = []
                teams = []
                positions = []
                max_season = 0
                position_innings = 0
                if type(season) == int:
                    year_id = season - 2025
                    for index, dictionary in enumerate(fielding):
                        if dictionary["league_year_id"] == year_id:
                            seasons.append(index)
                else:
                    for index, dictionary in enumerate(fielding):
                        if dictionary["league_year_id"] > max_season:
                            max_season = dictionary["league_year_id"]
                            seasons.clear()
                            seasons.append(index)
                        elif dictionary["league_year_id"] == max_season:
                            seasons.append(index)
                if type(team_abbreviation) == str:
                    teams.clear()
                    team = team_abbreviation.upper()
                    for index, dictionary in enumerate(fielding):
                        if dictionary["team_abbrev"] == team:
                            teams.append(index)
                else:
                    for index, dictionary in enumerate(fielding):
                        teams.append(index)
                if type(position) == str:
                    for index, dictionary in enumerate(fielding):
                        pos_upper = position.upper()
                        if dictionary["pos"] == pos_upper:
                            positions.append(index)
                else:
                    positions = sorted(range(len(fielding)), key=lambda i: fielding[i]["inn"], reverse=True)
                set_teams = set(teams)
                set_seasons = set(seasons)
                stats = next((item for item in positions if item in set_teams and item in set_seasons), None)
                if type(stats) is not int:
                    await interaction.followup.send(f"Could not find fielding stats for that player{' on that team' if type(team_abbreviation) == str else ''}{' at that position' if type(position) == str else ''}{' for that season' if type(season) == int else ''}")
                else:
                    title = f"{data['name']} {player['listed_position']} {id}"
                    if vis['pool'] == "college":
                        redshirt = False
                        if contract['years'] > 4:
                            redshirt = True
                        year = GetYear(contract['current_year'], redshirt)
                        desc = f"{year} from {bio['city']}, {bio['area']}"
                    else:
                        desc = f"{bio['age']} years old from {bio['city']}, {bio['area']}"

                    embed_player = discord.Embed(colour=discord.Colour.gold(),
                                        description=desc,
                                        title=title)
                    embed_player.set_footer(text="Simulation Sports Network")

                    embed_player.add_field(name="Team", value=fielding[stats]["team_abbrev"])
                    embed_player.add_field(name="Season", value=f"{fielding[stats]['league_year_id']+2025}")
                    embed_player.add_field(name="Position", value=fielding[stats]["pos"])
                    embed_player.add_field(name="Games Played", value=fielding[stats]["g"])
                    embed_player.add_field(name="Innings", value=fielding[stats]["inn"])
                    embed_player.add_field(name="Put Outs", value=fielding[stats]["po"])
                    embed_player.add_field(name="Assists", value=fielding[stats]["a"])
                    embed_player.add_field(name="Errors", value=fielding[stats]["e"])

                    await interaction.followup.send(embed=embed_player)
        except Exception as e:
            print(f"Error occured: {e}")
            
    @baseball_player_id_group.command(name="pitching_stats", description="Look up a players pitching stats using an {id} and optional {team abbreviation} and {season}")
    async def pitching_stats(self, interaction: discord.Interaction, id: int, team_abbreviation: typing.Optional[str] = None, season: typing.Optional[int] = None):
        try:
            await interaction.response.defer()
            data = api_requests.GetBaseballPlayer_id(id)
            player = api_requests.GetBaseballPlayer_id2(id)
            if data == False:
                await interaction.followup.send(f"Could not find player")
            else:
                pitching = data["pitching"]
                bio = player["bio"]
                contract = player["contract"]
                vis = player["visibility"]
                seasons = []
                teams = []
                max_season = 0
                if type(season) == int:
                    year_id = season - 2025
                    for index, dictionary in enumerate(pitching):
                        if dictionary["league_year_id"] == year_id:
                            seasons.append(index)
                else:
                    for index, dictionary in enumerate(pitching):
                        if dictionary["league_year_id"] > max_season:
                            max_season = dictionary["league_year_id"]
                            seasons.clear()
                            seasons.append(index)
                        elif dictionary["league_year_id"] == max_season:
                            seasons.append(index)
                if type(team_abbreviation) == str:
                    team = team_abbreviation.upper()
                    for index, dictionary in enumerate(pitching):
                        if dictionary["team_abbrev"] == team:
                            teams.append(index)
                else:
                    for index, dictionary in enumerate(pitching):
                        teams.append(index)
                stats_set = set(seasons) & set(teams)
                if not stats_set:
                    await interaction.followup.send(f"Could not find pitching stats for that player{' on that team' if type(team_abbreviation) == str else ''}{' for that season' if type(season) == int else ''}")
                else:
                    stats = stats_set.pop()
                    title = f"{data['name']} {player['listed_position']} {id}"
                    if vis['pool'] == "college":
                        redshirt = False
                        if contract['years'] > 4:
                            redshirt = True
                        year = GetYear(contract['current_year'], redshirt)
                        desc = f"{year} from {bio['city']}, {bio['area']}"
                    else:
                        desc = f"{bio['age']} years old from {bio['city']}, {bio['area']}"

                    embed_player = discord.Embed(colour=discord.Colour.gold(),
                                        description=desc,
                                        title=title)
                    embed_player.set_footer(text="Simulation Sports Network")

                    embed_player.add_field(name="Team", value=pitching[stats]["team_abbrev"])
                    embed_player.add_field(name="Season", value=f"{pitching[stats]['league_year_id']+2025}")
                    embed_player.add_field(name="Games Played", value=pitching[stats]["g"])
                    embed_player.add_field(name="Games Started", value=pitching[stats]["gs"])
                    embed_player.add_field(name="Innings Pitched", value=pitching[stats]["ip"])
                    embed_player.add_field(name="Quality Starts", value=pitching[stats]["qs"])
                    embed_player.add_field(name="Record", value=f"{pitching[stats]['w']}-{pitching[stats]['l']}")
                    embed_player.add_field(name="Holds", value=pitching[stats]["hld"])
                    embed_player.add_field(name="Saves", value=pitching[stats]["sv"])
                    embed_player.add_field(name="Earned Runs", value=pitching[stats]["er"])
                    embed_player.add_field(name="ERA", value=pitching[stats]["era"])
                    embed_player.add_field(name="Strike Outs", value=pitching[stats]["so"])
                    embed_player.add_field(name="Walks", value=pitching[stats]["bb"])
                    embed_player.add_field(name="Hits Allowed", value=pitching[stats]["h"])
                    embed_player.add_field(name="Home Runs Allowed", value=pitching[stats]["hr"])

                    await interaction.followup.send(embed=embed_player)
        except Exception as e:
            print(f"Error occured: {e}")
            
async def setup(client: commands.Bot):
    await client.add_cog(baseball_player_id(client))
