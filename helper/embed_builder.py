import discord
### FOR STREAMING

def Get_CBB_Play_Embed(play, home_abbr, away_abbr, home_url, away_url, home_score, away_score, injury_url):
    type_of_play = play["TypeOfPlay"]
    time_remaining = play["TimeRemaining"]
    possession = play["Possession"]
    result = play["Result"]
    desc = f"Current Score: {home_abbr} {home_score} - {away_abbr} {away_score}"
    embed_url = ""
    if possession == home_abbr:
        embed_url = home_url
    else:
        embed_url = away_url
    if type_of_play == "Injury":
        embed_url = injury_url
    embed = discord.Embed(colour=discord.Colour.orange(),description=desc,title="Play")
    embed.add_field(name="Type of Play", value=f"{type_of_play}", inline=False)
    embed.add_field(name=f"Possessions Remaining: {time_remaining}", value=f"Possession: {possession}", inline=False)
    embed.add_field(name="Result", value=f"{result}", inline=False)    
    embed.set_thumbnail(url=embed_url)
    return embed

def Get_FBA_Play_Embed(play, home_abbr, away_abbr, home_url, away_url, home_score, away_score, result):
    play_num = play["PlayNumber"]
    home_score = play["HomeTeamScore"]
    away_score = play["AwayTeamScore"]
    quarter = play["Quarter"]
    time_remaining = play["TimeRemaining"]
    distance = play["Distance"]
    line_of_scrimmage = play["LineOfScrimmage"]
    play_type = play["PlayType"]
    play_name = play["PlayName"]
    off_formation = play["OffensiveFormation"]
    def_formation = play["DefensiveFormation"]
    point_of_attack = play["PointOfAttack"]
    def_tendency = play["DefensiveTendency"]
    blitz_number = play["BlitzNumber"]
    lb_cov = play["LBCoverage"]
    db_cov = play["CBCoverage"]
    s_cov = play["SCoverage"]
    res_yards = play["ResultYards"]
    time_remaining = play["TimeRemaining"]
    possession = play["Possession"]
    distance = play["Distance"]
    down_input = play["Down"]
    down = get_down(down_input)
    if play_type == "Kick Off":
        down = ""
    line_of_scrimmage = play["LineOfScrimmage"]
    desc = f"Current Score: {home_abbr} {home_score} - {away_abbr} {away_score}"
    embed_url = ""
    if possession == home_abbr:
        embed_url = home_url
    else:
        embed_url = away_url
    embed = discord.Embed(colour=discord.Colour.dark_gold(),description=desc,title=f"Play {play_num}")
    embed.add_field(name=f"Possessions Remaining: {time_remaining}, {quarter}Q", value=f"Possession: {possession}", inline=False)
    embed.add_field(name=f"{down} and {distance}", value=f"Line of Scrimmage: {line_of_scrimmage}", inline=False)
    embed.add_field(name="Play Type", value=f"{play_type}", inline=False)
    embed.add_field(name="Play Name", value=f"{play_name}", inline=True)
    embed.add_field(name="Point of Attack", value=f"{point_of_attack}", inline=True)
    embed.add_field(name="Defensive Tendency", value=f"{def_tendency}", inline=True)
    embed.add_field(name="Offensive Formation", value=f"{off_formation}", inline=True)
    embed.add_field(name="Defensive Formation", value=f"{def_formation}", inline=True)
    embed.add_field(name="Blitz Number", value=f"{blitz_number}", inline=False)
    embed.add_field(name="LB Coverage", value=f"{lb_cov}", inline=True)
    embed.add_field(name="CB Coverage", value=f"{db_cov}", inline=True)
    embed.add_field(name="S Coverage", value=f"{s_cov}", inline=True)
    embed.add_field(name="Resulting Yards", value=f"{res_yards}", inline=False)
    embed.add_field(name="Result", value=f"{result}", inline=False)    
    embed.set_thumbnail(url=embed_url)
    return embed

def get_down(down):
    if down == "1" or down == 1:
        return "1st Down"
    elif down == "2"or down == 2:
        return "2nd Down"
    elif down == "3"or down == 3:
        return "3rd Down"
    elif down == "4"or down == 4:
        return "4th Down"
    return "IT'S 5TH DOWN EVERYBODY!"

def Get_Hockey_Play_Embed(play, home_abbr, away_abbr, home_url, away_url, home_score, away_score, injury_url, penalty_url):
    period = play["Period"]
    zone = play["Zone"]
    event = play["Event"]
    penalty = play["Penalty"]
    severity = play["Severity"]
    time_remaining = play["TimeOnClock"]
    time_consumed = play["SecondsConsumed"]
    team_id = play["TeamID"]
    possession = home_abbr
    if team_id == play["AwayTeamID"]:
        possession = away_abbr
    result = play["Result"]
    desc = f"Current Score: {home_abbr} {home_score} - {away_abbr} {away_score}"
    embed_url = ""
    if possession == home_abbr:
        embed_url = home_url
    else:
        embed_url = away_url
    if event == "Penalty Check":
        embed_url = penalty_url
    if event == "Injury":
        embed_url = injury_url
    embed = discord.Embed(colour=discord.Colour.light_gray(),description=desc,title="Play")
    embed.add_field(name=f"Period: {period}", value=f"Time: {time_remaining}", inline=True)
    embed.add_field(name=f"Time Passed", value=f"{time_consumed}", inline=True)
    embed.add_field(name="Zone", value=f"{zone}", inline=True)
    embed.add_field(name="Event", value=f"{event}", inline=False)

    if event == "Penalty Check":
        embed.add_field(name="Case", value=f"{penalty}", inline=True)
        embed.add_field(name="Severity", value=f"{severity}", inline=True)
    embed.add_field(name="Result", value=f"{result}", inline=False)    
    embed.set_thumbnail(url=embed_url)
    return embed
