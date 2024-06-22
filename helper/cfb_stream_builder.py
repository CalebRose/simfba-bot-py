import discord
import os
import csv
from helper import embed_builder, util, message_sender
import constants
import logos_util
import asyncio
from api_requests import StreamFootballGames

async def stream_fb_game(chan, league: str, timeslot: str, week: str, isNFL):
    streams = StreamFootballGames(league, timeslot, week, isNFL)
    injury_url = logos_util.GetIcon("Injury")
    penalty_url = logos_util.GetIcon("Penalty")
    
    for game in streams:
        total_rows = game["Streams"]
        home_team = game["HomeTeam"]
        home_id = game["HomeTeamID"]
        home_rank = game["HomeTeamRank"]
        home_coach = game["HomeTeamCoach"]
        home_label = game["HomeLabel"]
        home_tag = game["HomeTeamDiscordID"]
        home_os = game["HomeOffensiveScheme"]
        home_ds = game["HomeDefensiveScheme"]
        away_team = game["AwayTeam"]
        away_tag = game["AwayTeamDiscordID"]
        away_rank = game["AwayTeamRank"]
        away_coach = game["AwayTeamCoach"]
        away_label = game["AwayLabel"]
        away_os = game["AwayOffensiveScheme"]
        away_ds = game["AwayDefensiveScheme"]
        cloud = game["GameCloud"]
        wind = game["GameWind"]
        precip = game["GamePrecip"]
        wind_speed = game["GameWindSpeed"]
        temp = game["GameTemp"]
        stadium = game["Stadium"]
        city = game["City"]
        state = game["State"]
        home_ranked_str = ""
        if home_rank > 0:
            home_ranked_str=f"({home_rank}) "
        away_ranked_str = ""
        if away_rank > 0:
            away_ranked_str=f"({away_rank}) "
        contending_teams_str = ""
        hc_label = home_coach.strip()
        ac_label = away_coach.strip()
        if home_tag != "":
            hc_label = home_tag
        if away_tag != "":
            ac_label = away_tag
        
        contending_teams_str = f"Home Team: {home_ranked_str}{home_team} | Coach: {hc_label}"
        contending_teams_str += f"\nAway Team: {away_ranked_str}{away_team} | Coach: {ac_label}"
        scheme_string = f"Home Offense: {home_os.strip()} | Home Defensive: {home_ds.strip()}"
        scheme_string += f"\nAway Offense: {away_os.strip()} | Away Defensive: {away_ds.strip()}"
        location_str = f"{stadium} in {city}, {state}"
        rain_str = ""
        if precip == "Clear":
            rain_str = "no chance of rain and "
        elif precip == "Drizzling":
            rain_str = "a bit of a drizzle and "
        elif precip == "Light Rain Rain":
            rain_str = "some light rain and "
        elif precip == "Moderate Rain":
            rain_str = "rain and "
        elif precip == "Heavy Rain":
            rain_str = "heavy rainfall and "
        weather_str = f"{str(round(temp,2))} degrees Fahrenheit, {cloud} Skies with {rain_str}{wind} with speeds around {str(round(wind_speed, 2))}mph"
        f_home_score = 0
        f_away_score = 0
        ### Logos
        if league == 'cfb':
            home_team_id = id_util.GetCollegeFootballTeamID(home_team.strip().upper())
            home_url = logos_util.GetCFBLogo(home_team_id)
            away_team_id = id_util.GetCollegeFootballTeamID(away_team.strip().upper())
            away_url = logos_util.GetCFBLogo(away_team_id)
        elif league == 'nfl':
            home_team_id = id_util.GetNFLTeamID(home_team.strip().upper())
            home_url = logos_util.GetNFLLogo(home_team_id)
            away_team_id = id_util.GetNFLTeamID(away_team.strip().upper())
            away_url = logos_util.GetNFLLogo(away_team_id)
        announcer = util.PickAnnouncer(league, home_id)
        announcer_url = logos_util.GetAnnouncer(announcer)
        intro_text = util.AnnouncerIntroText(announcer, home_label, away_label, 'CFB', stadium)

        ### Build Announcer Embed
        init_embed = discord.Embed(colour=discord.Colour.blue(),description=intro_text,title=f"Streaming {home_label} Match!")
        init_embed.add_field(name="Announcer", value=announcer, inline=False)
        init_embed.set_thumbnail(url=announcer_url)
        await message_sender.SendEmbedMessage(chan, init_embed)

        await asyncio.sleep(5)

        await message_sender.SendMessage(chan, contending_teams_str)

        await asyncio.sleep(5)

        ### Build Initial Game Embed
        init_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title="Streaming SimCFB Match!")
        init_embed.add_field(name="Location", value=location_str, inline=False)
        init_embed.add_field(name="Weather", value=weather_str, inline=False)
        init_embed.add_field(name="Schemes", value=scheme_string, inline=False)
        init_embed.set_thumbnail(url=home_url)

        await message_sender.SendEmbedMessage(chan, init_embed)

        await asyncio.sleep(10)

        for idx, play in enumerate(total_rows):
            home_score = play["HomeTeamScore"]
            away_score = play["AwayTeamScore"]
            f_home_score = home_score
            f_away_score = away_score
            stream_results = play["StreamResult"]

            for i, s in enumerate(stream_results):
                is_injury = util.IsInjury(s)
                is_penalty = util.IsPenalty(s)
                is_redzone = util.IsRedzone(s)

                if is_injury == True:
                    ## One message sent
                    injury_embed = discord.Embed(colour=discord.Colour.red(),description="Uh oh! Looks like there's an injury on the field.",title="Injury!")
                    injury_embed.set_thumbnail(url=injury_url)
                    await message_sender.SendEmbedMessage(chan, injury_embed)
                    await asyncio.sleep(5)
                    actual_injury_embed = discord.Embed(colour=discord.Colour.red(),description=s,title="Injury!")
                    actual_injury_embed.set_thumbnail(url=injury_url)
                    await message_sender.SendEmbedMessage(chan, actual_injury_embed)
                    await asyncio.sleep(10)
                    
                elif is_penalty == True:
                    ## Generate Text for Penalties, two messages sent
                    intro_penalty_text = util.GetIntroPenaltyStr()
                    penalty_embed = discord.Embed(colour=discord.Colour.yellow(),description=intro_penalty_text,title="PENALTY!")
                    penalty_embed.set_thumbnail(url=penalty_url)
                    await message_sender.SendEmbedMessage(chan, penalty_embed)
                    await asyncio.sleep(5)
                    actual_penalty_embed = discord.Embed(colour=discord.Colour.yellow(),description=s,title="PENALTY!")
                    actual_penalty_embed.set_thumbnail(url=penalty_url)
                    await message_sender.SendEmbedMessage(chan, actual_penalty_embed)
                    await asyncio.sleep(10)
                else:
                    if is_redzone == True:
                        await message_sender.SendMessage(chan, "REDZONE ALERT: <@&1235669913478365244>")
                        await asyncio.sleep(5)

                    play_embed = embed_builder.Get_FBA_Play_Embed(play, home_team, away_team, home_url, away_url, home_score, away_score, s)
                    await message_sender.SendEmbedMessage(chan, play_embed)
                    await asyncio.sleep(8)
        
        final_score = f"{home_label}: {f_home_score} | {away_label}: {f_away_score}"
        final_title = "... and that's the game, folks! Thank you for watching!"
        final_url = ""
        if f_home_score > f_away_score:
            final_url = home_url
        else:
            final_url = away_url
        final_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title=final_title)
        final_embed.add_field(name="Final Score", value=final_score, inline=False)
        final_embed.set_thumbnail(url=final_url)
        await message_sender.SendEmbedMessage(chan, final_embed)
        await asyncio.sleep(30)
                                                    
    await message_sender.SendMessage(chan, f"That's all the games for today, thank you for watching!")
