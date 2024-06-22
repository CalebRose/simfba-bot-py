import discord
import os
import csv
from helper import embed_builder
import constants
import logos_util
import asyncio

async def stream_game(chan, channel: str, week: str):
    game_directory = os.path.normpath(os.path.join(constants.base_nfl_simulation_path, f"Week {week}", channel))
    if os.path.exists(game_directory):
        list_of_games = os.listdir(game_directory)
        for game_folder in list_of_games:
            game_path = os.path.normpath(os.path.join(game_directory, game_folder))
            games_files = os.listdir(game_path)
            for file in games_files:
                file_name = file.replace(" Play-By-Play.csv", "")
                teams = file_name.split(" vs ")
                home_team_name = teams[0]
                away_team_name = teams[1]
                if file.endswith('Play-By-Play.csv'):
                    game_file_path = os.path.normpath(os.path.join(game_path, file))
                    with open(game_file_path, newline="") as game:
                        reader = csv.reader(game, delimiter=",", quotechar="|")
                        total_rows = list(reader)
                        contending_teams_str = ""
                        final_score = ""
                        count = 0
                        results = []
                        scheme_string = ""
                        for row in total_rows:
                            if count == 0:
                                home_team_abbr = row[0].strip()
                                away_team_abbr = row[1].strip()
                                contending_teams_str = f"Home Team: {home_team_abbr} | Away Team: {away_team_abbr}"
                            elif count == 1:
                                contending_teams_str += f"\nHome Coach: {row[1].strip()} | Away Coach: {row[3].strip()}"
                            elif count == 2:
                                scheme_string = f"Home Offensive Scheme: {row[1].strip()} | Away Offensive Scheme: {row[3].strip()}"
                            elif count == 3:
                                scheme_string += f"\nHome Defensive Scheme: {row[1].strip()} | Away Defensive Scheme: {row[3].strip()}"
                            elif count == 4:
                                final_score = f"{home_team_abbr}: {row[1]} | {away_team_abbr}: {row[3].strip()}"
                            elif count == 5 or count == len(total_rows) - 1:
                                ...
                            else:
                                score = {
                                    "HomeScore": row[0],
                                    "AwayScore": row[1],
                                    "Quarter": row[2],
                                    "TimeRemaining": row[3],
                                    "Down": row[5],
                                    "Distance": row[6],
                                    "LineOfScrimmage": row[7],
                                    "TypeOfPlay": row[8],
                                    "Result": row[9].strip(),
                                    "Possession": row[4]
                                }
                                results.append(score)
                            count += 1

                        ### Logos
                        home_team_id = id_util.GetNFLTeamID(home_team.strip().upper())
                        home_url = logos_util.GetNFLLogo(home_team_id)
                        away_team_id = id_util.GetNFLTeamID(away_team.strip().upper())
                        away_url = logos_util.GetNFLLogo(away_team_id)

                        ### Build Initial Embed
                        init_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title="Streaming SimNFL Match!")
                        init_embed.add_field(name="Schemes", value=scheme_string, inline=False)
                        init_embed.set_thumbnail(url=home_url)
                        await chan.send(embed=init_embed)

                        await asyncio.sleep(5)

                        home_score = 0
                        away_score = 0

                        for play in results:
                            home_score = play['HomeScore']
                            away_score = play['AwayScore']
                            play_embed = embed_builder.Get_FBA_Play_Embed(play, home_team_name, away_team_name, home_url, away_url, home_score, away_score)
                            await chan.send(embed=play_embed)
                            await asyncio.sleep(8)
                        
                        final_title = "... and that's the game, folks! Thank you for watching!"
                        final_url = ""
                        if home_score > away_score:
                            final_url = home_url
                        else:
                            final_url = away_url
                        final_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title=final_title)
                        final_embed.add_field(name="Final Score", value=final_score, inline=False)
                        final_embed.set_thumbnail(url=final_url)
                        await chan.send(embed=final_embed)
                        await asyncio.sleep(30)
                                                    

        await chan.send(f"That's all the games for today, thank you for watching!")
