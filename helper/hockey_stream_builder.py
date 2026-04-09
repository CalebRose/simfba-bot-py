import discord
import os
import csv
import api_requests
from helper import embed_builder, message_sender, util
import constants
import logos_util
import id_util
import asyncio
from api_requests import StreamHockeyGames, RevealHCKGameResultsOnInterface

async def stream_hockey_game(chan, channel: str, league: str):
    is_pro = league == 'phl'
    streams = StreamHockeyGames(is_pro,channel)
    injury_url = logos_util.GetIcon("Injury")
  
    for game in streams:
        total_rows = game["Streams"]
        home_team = game["HomeTeam"]
        home_id = game["HomeTeamID"]
        home_rank = game["HomeTeamRank"]
        home_coach = game["HomeTeamCoach"]
        home_label = game["HomeLabel"]
        home_tag = game["HomeTeamDiscordID"]
        away_id = game["AwayTeamID"]
        away_team = game["AwayTeam"]
        away_tag = game["AwayTeamDiscordID"]
        away_rank = game["AwayTeamRank"]
        away_coach = game["AwayTeamCoach"]
        away_label = game["AwayLabel"]
        game_label = game["GameLabel"]
        arena = game["Arena"]
        city = game["City"]
        state = game["State"]
        country = game["Country"]
        arena = game["Arena"]
        attendance = game["Attendance"]
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
        ### Logos
        home_url = ""
        away_url = ""
        if is_pro:
            home_url = logos_util.GetPHLLogo(int(home_id))
            away_url = logos_util.GetPHLLogo(int(away_id))    
        else:
            home_url = logos_util.GetCHLLogo(int(home_id))
            away_url = logos_util.GetCHLLogo(int(away_id))
        announcer = util.PickHKAnnouncer()
        announcer_url = logos_util.GetAnnouncer(announcer)
        intro_text = util.HKAnnouncerIntroText(announcer, home_label, away_label, league, arena)

        ### Build Announcer Embed
        init_embed = discord.Embed(colour=discord.Colour.blue(),description=intro_text,title=f"Streaming {home_label} Match!")
        init_embed.add_field(name="Announcer", value=announcer, inline=False)
        init_embed.set_thumbnail(url=announcer_url)
        await message_sender.SendEmbedMessage(chan, init_embed)
        await asyncio.sleep(3)

        ### Build Initial Embed
        game_embed = discord.Embed(colour=discord.Colour.light_gray(),description=contending_teams_str,title="Streaming College Hockey Game!")
        if len(game_label) > 0:
            game_embed.add_field(name="Match Name", value=f"{game_label}", inline=False)
        game_embed.add_field(name=f"{arena}", value=f"{city}, {state}, {country}", inline=False)
        game_embed.add_field(name=f"Home Coach", value=f"{home_coach}", inline=True)
        game_embed.add_field(name=f"Away Coach", value=f"{away_coach}", inline=True)

        game_embed.set_thumbnail(url=home_url)
        await message_sender.SendEmbedMessage(chan, embed=game_embed)
        await asyncio.sleep(1)
        await message_sender.SendMessage(chan, contending_teams_str)
        await asyncio.sleep(5)
        home_score = 0
        away_score = 0

        for idx, play in enumerate(total_rows):
            time_consumed = 2
            outcome = play["Outcome"]
            if outcome == "Goalie Hold":
                time_consumed = 5
            elif outcome == "Shot on Goal":
                time_consumed = 10
            elif outcome == "Shootout":
                time_consumed = 10
            elif outcome == "EnteringShootout":
                time_consumed = 10
            elif outcome == "No One Open":
                continue
            home_score = play['HomeTeamScore']
            away_score = play['AwayTeamScore']
            play_embed = embed_builder.Get_Hockey_Play_Embed(play, home_team, away_team, home_url, away_url, home_score, away_score, injury_url)
            await message_sender.SendEmbedMessage(chan, embed=play_embed)
            await asyncio.sleep(int(time_consumed))
        
        final_title = "... and that's the game, folks! Thank you for watching!"
        final_score = f"{home_score}-{away_score}"
        final_url = ""
        if home_score > away_score:
            final_url = home_url
        else:
            final_url = away_url
        final_embed = discord.Embed(colour=discord.Colour.light_gray(),description=contending_teams_str,title=final_title)
        final_embed.add_field(name="Final Score", value=final_score, inline=False)
        final_embed.add_field(name="Syncing results...", value="Check the Interface for results & a post-game discussion!", inline=False)
        final_embed.set_thumbnail(url=final_url)
        await message_sender.SendEmbedMessage(chan, embed=final_embed)
        RevealHCKGameResultsOnInterface(is_pro, game["ID"])

        await asyncio.sleep(10)
                                            

    await chan.send(f"That's all for today's games, folks!")
