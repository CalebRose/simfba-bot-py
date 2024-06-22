import discord
import os
import csv
from helper import embed_builder, message_sender
import constants
import logos_util
import asyncio

async def stream_game(chan, channel: str, week: str, day: str):
    day_uppercase = day.upper()
    week_directory = os.path.normpath(os.path.join(constants.base_simulation_path, channel, f"Week {week}", day_uppercase))
    play_by_play_directory = os.path.normpath(os.path.join(week_directory, "play_by_plays"))
    if os.path.exists(play_by_play_directory):
        list_of_games = os.listdir(play_by_play_directory)
        for filename in list_of_games:
            contending_teams_str = ""
            home_team_abbr = ""
            away_team_abbr = ""
            final_score = ""
            count = 0
            results = []
            home_offensive_style = ""
            home_offensive_formation = ""
            home_defensive_formation = ""
            home_pace = ""
            home_coach = ""
            away_offensive_style = ""
            away_offensive_formation = ""
            away_defensive_formation = ""
            away_pace = ""
            away_coach = ""
            match_name = ""
            arena = ""
            city = ""
            state = ""
            if filename.endswith('.csv'):
                game_path = os.path.normpath(os.path.join(play_by_play_directory, filename))
                with open(game_path, newline="") as game:
                    reader = csv.reader(game, delimiter=",", quotechar="|")
                    total_rows = list(reader)
                    for row in total_rows:
                        if count == 1:
                            home_team_abbr = row[0].strip()
                            away_team_abbr = row[1].strip()
                            contending_teams_str = f"Home Team: {home_team_abbr} | Away Team: {away_team_abbr}"
                            final_score = f"{home_team_abbr}: {row[2]} | {away_team_abbr}: {row[3].strip()}"
                            home_coach = row[5]
                            home_offensive_style = row[6]
                            home_offensive_formation = row[7]
                            home_defensive_formation = row[8]
                            home_pace = row[9]
                            away_coach = row[10]
                            away_offensive_style = row[11]
                            away_offensive_formation = row[12]
                            away_defensive_formation = row[13]
                            away_pace = row[14]
                            match_name = row[15]
                            arena = row[16]
                            city = row[17]
                            state = row[18]
                        elif count == 0 or count == 2 or count == 3 or count == len(total_rows) - 1 or len(row) < 3:
                            count += 1
                            continue
                        else:
                            time_remaining = int(row[6].strip()) - int(row[5].strip()) + 1
                            score = {
                                "HomeScore": row[3],
                                "AwayScore": row[4],
                                "TimeRemaining": time_remaining,
                                "TypeOfPlay": row[2],
                                "Result": row[1].strip(),
                                "Possession": row[0].strip()
                            }
                            results.append(score)
                        count += 1
                        
                    if len(home_coach) == 0:
                        home_coach = "AI"
                    if len(away_coach) == 0:
                        away_coach = "AI"

                    ### Logos
                    home_team_id = id_util.GetNBATeamID(home_team_abbr.upper())
                    home_url = logos_util.GetNBALogo(home_team_id)
                    away_team_id = id_util.GetNBATeamID(away_team_abbr.upper())
                    away_url = logos_util.GetNBALogo(away_team_id)

                    ### Build Initial Embed
                    init_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title="Streaming CBB Match Live on CBS!")
                    if len(match_name) > 0:
                        init_embed.add_field(name="Match Name", value=f"{match_name}", inline=False)
                    init_embed.add_field(name=f"{arena}", value=f"{city}, {state}", inline=False)
                    init_embed.add_field(name=f"Home Coach: {home_coach}", value=f"Pace: {home_pace}", inline=True)
                    init_embed.add_field(name="Home Offensive Style", value=f"{home_offensive_style}", inline=True)
                    init_embed.add_field(name="Home Offensive Formation", value=f"{home_offensive_formation}", inline=True)
                    init_embed.add_field(name="Home Defensive Formation", value=f"{home_defensive_formation}", inline=False)
                    init_embed.add_field(name=f"Away Coach: {away_coach}", value=f"Pace: {away_pace}", inline=True)
                    init_embed.add_field(name="Away Offensive Style", value=f"{away_offensive_style}", inline=True)
                    init_embed.add_field(name="Away Offensive Formation", value=f"{away_offensive_formation}", inline=True)
                    init_embed.add_field(name="Away Defensive Formation", value=f"{away_defensive_formation}", inline=False)
                    init_embed.set_thumbnail(url=home_url)
                    await message_sender.SendEmbedMessage(chan, embed=init_embed)

                    home_score = 0
                    away_score = 0

                    for play in results:
                        home_score = play['HomeScore']
                        away_score = play['AwayScore']
                        type_of_play = play["TypeOfPlay"]
                        if type_of_play == "HALFTIME":
                            embed_url = ""
                            end_of_quarter_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title="... and that brings us to halftime, folks! We'll be back in a few seconds!")
                            if int(home_score) > int(away_score):
                                embed_url = home_url
                            else:
                                embed_url = away_url
                            end_of_quarter_embed.add_field(name="Score Board", value=f"Current Score: {home_team_abbr} {home_score} - {away_team_abbr} {away_score}", inline=True)
                            end_of_quarter_embed.set_thumbnail(url=embed_url)
                            await message_sender.SendEmbedMessage(chan, embed=end_of_quarter_embed)
                        elif type_of_play == "FinalScore":
                            continue
                        elif type_of_play == "END OF 1ST QUARTER":
                            embed_url = ""
                            end_of_quarter_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title="... and that brings us to end of the 1st Quarter, folks! We'll be back in a few seconds!")
                            if int(home_score) > int(away_score):
                                embed_url = home_url
                            else:
                                embed_url = away_url
                            end_of_quarter_embed.add_field(name="Score Board", value=f"Current Score: {home_team_abbr} {home_score} - {away_team_abbr} {away_score}", inline=True)
                            end_of_quarter_embed.set_thumbnail(url=embed_url)
                            await message_sender.SendEmbedMessage(chan, embed=end_of_quarter_embed)
                        elif type_of_play == "END OF 3RD QUARTER":
                            embed_url = ""
                            end_of_quarter_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title="... and that brings us to end of the 3rd Quarter, folks! We'll be back in a few seconds!")
                            if int(home_score) > int(away_score):
                                embed_url = home_url
                            else:
                                embed_url = away_url
                            end_of_quarter_embed.add_field(name="Score Board", value=f"Current Score: {home_team_abbr} {home_score} - {away_team_abbr} {away_score}", inline=True)
                            end_of_quarter_embed.set_thumbnail(url=embed_url)
                            await message_sender.SendEmbedMessage(chan, embed=end_of_quarter_embed)
                        else:
                            play_embed = embed_builder.Get_CBB_Play_Embed(play, home_team_abbr, away_team_abbr, home_url, away_url, home_score, away_score)
                            await message_sender.SendEmbedMessage(chan, embed=play_embed)
                        if type_of_play == "Tipoff" or type_of_play == "FreeThrow":
                            await asyncio.sleep(2)
                        elif type_of_play == "Turnover":
                            await asyncio.sleep(2)
                        elif type_of_play == "Score" or type_of_play == "Missed" or type_of_play == "Miss":
                            await asyncio.sleep(4)
                        elif type_of_play == "Shot Clock" or type_of_play == "Out of Bounds" or type_of_play == "Fouled":
                            await asyncio.sleep(8)
                        elif type_of_play == "HALFTIME" or type_of_play == "OVERTIME" or type_of_play == "END OF 1ST QUARTER" or type_of_play == "END OF 3RD QUARTER":
                            await asyncio.sleep(15)
                        else:
                            await asyncio.sleep(4)
                    
                    final_title = "... and that's the game, folks! Thank you for watching!"
                    final_url = ""
                    if home_score > away_score:
                        final_url = home_url
                    else:
                        final_url = away_url
                    final_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title=final_title)
                    final_embed.add_field(name="Final Score", value=final_score, inline=False)
                    final_embed.set_thumbnail(url=final_url)
                    await message_sender.SendEmbedMessage(chan, embed=final_embed)
                    await asyncio.sleep(30)

        await chan.send(f"That's all the games for today, thank you for watching!")
