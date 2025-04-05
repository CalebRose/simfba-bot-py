import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests

class assign_id(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cfb_register", description="Register to your CFB team so you will be tagged when games stream!")
    async def cfb_register(self, interaction: discord.Interaction, team: str):
        try:
            upper_input = team.upper()
            team_id = id_util.GetCollegeFootballTeamID(upper_input)
            logo_url = logos_util.GetCFBLogo(team_id)

            discord_id = interaction.user.mention
            res = api_requests.RegisterFBTeam(False, team_id, discord_id)
            if res == True:
                embed = discord.Embed(colour=discord.Colour.dark_gold(),
                    description=f"Congratulations! You will now be pinged whenever {team}'s games are streamed.",
                    title=f"Successfully Registered to {team}!")
                embed.set_thumbnail(url=logo_url)
                await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(colour=discord.Colour.dark_gold(),
                    description=f"Don't worry, you did nothing wrong. Something technical occurred and will be resolved. Please post in forums for details.",
                    title=f"Error! Could not register to {team}!")
                embed.set_thumbnail(url=logo_url)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

    @app_commands.command(name="nfl_register", description="Register to your NFL team so you will be tagged when games stream!")
    async def nfl_register(self, interaction: discord.Interaction, team: str):
        try:
            upper_input = team.upper()
            team_id = id_util.GetNFLTeamID(upper_input)
            logo_url = logos_util.GetNFLLogo(team_id)

            discord_id = interaction.user.mention
            res = api_requests.RegisterFBTeam(True, team_id, discord_id)
            if res == True:
                embed = discord.Embed(colour=discord.Colour.dark_gold(),
                    description=f"Congratulations! You will now be pinged whenever {team}'s games are streamed.",
                    title=f"Successfully Registered to {team}!")
                embed.set_thumbnail(url=logo_url)
                await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(colour=discord.Colour.dark_gold(),
                    description=f"Don't worry, you did nothing wrong. Something technical occurred and will be resolved. Please post in forums for details.",
                    title=f"Error! Could not register to {team}!")
                embed.set_thumbnail(url=logo_url)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

    @app_commands.command(name="cbb_register", description="Register to your CBB team so you will be tagged when games stream!")
    async def cbb_register(self, interaction: discord.Interaction, team: str, username: str):
        try:
            upper_input = team.upper()
            team_id = id_util.GetCollegeBasketballTeamID(upper_input)
            logo_url = logos_util.GetCBBLogo(team_id)

            discord_id = interaction.user.mention
            res = api_requests.RegisterBBTeam(False, team_id, discord_id, username)
            if res == True:
                embed = discord.Embed(colour=discord.Colour.dark_gold(),
                    description=f"Congratulations! You will now be pinged whenever {team}'s games are streamed.",
                    title=f"Successfully Registered to {team}!")
                embed.set_thumbnail(url=logo_url)
                await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(colour=discord.Colour.dark_gold(),
                    description=f"Don't worry, you did nothing wrong. Something technical occurred and will be resolved. Please post in forums for details.",
                    title=f"Error! Could not register to {team}!")
                embed.set_thumbnail(url=logo_url)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

    @app_commands.command(name="nba_register", description="Register to your NBA team so you will be tagged when games stream!")
    async def nba_register(self, interaction: discord.Interaction, team: str, username: str):
        try:
            upper_input = team.upper()
            team_id = id_util.GetNBATeamID(upper_input)
            logo_url = logos_util.GetNBALogo(team_id)

            discord_id = interaction.user.mention
            res = api_requests.RegisterBBTeam(True, team_id, discord_id, username)
            if res == True:
                embed = discord.Embed(colour=discord.Colour.dark_gold(),
                    description=f"Congratulations! You will now be pinged whenever {team}'s games are streamed.",
                    title=f"Successfully Registered to {team}!")
                embed.set_thumbnail(url=logo_url)
                await interaction.response.send_message(embed=embed)
            else:
                embed = discord.Embed(colour=discord.Colour.dark_gold(),
                    description=f"Don't worry, you did nothing wrong. Something technical occurred and will be resolved. Please post in forums for details.",
                    title=f"Error! Could not register to {team}!")
                embed.set_thumbnail(url=logo_url)
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(assign_id(client))
