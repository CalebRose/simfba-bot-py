import discord
from helper.footer import _FOOTER
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


_BB_EVENT_LABELS = {
    "Tipoff": "Tip-Off",
    "Ot_tipoff": "Overtime Tip-Off",
    "Steal": "Steal",
    "Turnover": "Turnover",
    "Move": "Dribble Move",
    "Pass_ball": "Pass",
    "Heave": "Heave",
    "Free_throw": "Free Throw",
    "Shot_three": "Three-Pointer",
    "Shot_corner_three": "Corner Three",
    "Shot_inside": "Inside Shot",
    "Shot_paint": "Shot in the Paint",
    "Shot_midrange": "Mid-Range Jumper",
    "QuarterOver": "End of Quarter",
    "HalfOver": "Halftime",
    "GameOver": "End of Game",
    "OvertimeStart": "Overtime Start",
    "OvertimeOver": "End of Overtime",
    "Timeout": "Timeout",
    "Rebound": "Rebound",
    "Inbound": "Inbound",
}

_BB_SHOT_EVENTS = {"Shot_three", "Shot_corner_three", "Shot_inside", "Shot_paint", "Shot_midrange", "Heave", "Free_throw"}
_BB_MADE_OUTCOMES = {"Shot_made", "Shot_foul_made", "Heave_made", "Ft_made"}
_BB_MISSED_OUTCOMES = {"Shot_missed", "Shot_foul_missed", "Shot_blocked", "Shot_foul_blocked", "Heave_missed", "Ft_missed"}
_BB_TURNOVER_OUTCOMES = {"Pass_intercepted", "Steal_success", "Out_of_bounds_turnover", "Offensive_charge", "Shot_clock_violation", "Move_trapped"}
_BB_FOUL_OUTCOMES = {"Shot_foul_made", "Shot_foul_missed", "Shot_foul_blocked", "Move_foul", "Pass_foul", "Offensive_charge"}


def _bb_label(value):
    return str(value).replace("_", " ").strip()


def _bb_colour(event, outcome):
    if outcome in _BB_MADE_OUTCOMES:
        return discord.Colour.green()
    if outcome in _BB_MISSED_OUTCOMES:
        return discord.Colour.red()
    if outcome in _BB_TURNOVER_OUTCOMES:
        return discord.Colour.dark_orange()
    if event in ("QuarterOver", "HalfOver", "GameOver", "OvertimeStart", "OvertimeOver", "Timeout"):
        return discord.Colour.dark_gray()
    return discord.Colour.blue()

def Get_Timeout_Embed():
    # Decide which ad to play
    title = ""
    description = ""
    embed = discord.Embed(
        colour= discord.Colour.yellow(),
        description=description,
        title=title,
    )
    return embed

def Get_Basketball_Play_Embed(play, home_team, away_team, home_url, away_url, home_score, away_score, injury_url, penalty_url):
    event = play["Event"]
    outcome = play["Outcome"]
    quarter = play["Quarter"]
    time_remaining = play["TimeOnClock"]
    shot_clock = play["ShotClock"]
    seconds_consumed = play["SecondsConsumed"]
    play_num = play["PlayNumber"]
    injury_id = play["InjuryID"]
    penalty_id = play["PenaltyID"]

    stream_result = play["Result"]
    if not stream_result:
        result = play["StreamResult"] or []
        stream_result = "".join(result)
    if not stream_result:
        stream_result = _bb_label(outcome)

    is_home = play["TeamID"] == play["HomeTeamID"]
    possession = home_team if is_home else away_team
    embed_url = home_url if is_home else away_url
    if injury_id > 0:
        embed_url = injury_url
    elif outcome in _BB_FOUL_OUTCOMES and penalty_url:
        embed_url = penalty_url

    if event == "Substitution":
        return Get_Basketball_Substitution_Embed(play, home_team, away_team, home_score, away_score, embed_url)

    event_label = _BB_EVENT_LABELS.get(event, _bb_label(event))
    quarter_label = f"Q{quarter}" if quarter <= 4 else f"OT{quarter - 4}"

    embed = discord.Embed(
        colour=_bb_colour(event, outcome),
        description=f"**{home_team} {home_score} - {away_team} {away_score}**",
        title=f"Play {play_num}: {event_label}",
    )
    embed.add_field(name="Period", value=quarter_label, inline=True)
    embed.add_field(name="Game Clock", value=time_remaining, inline=True)
    embed.add_field(name="Shot Clock", value=str(shot_clock), inline=True)

    if injury_id > 0:
        embed.add_field(
            name="Injury",
            value=f"Type {play['InjuryType']}, out {play['InjuryDuration']} game(s)",
            inline=False,
        )
    if penalty_id > 0:
        embed.add_field(name="Penalty", value=f"Penalty ID {penalty_id}", inline=False)

    embed.add_field(name="Result", value=stream_result, inline=False)

    court = _FOOTER.get((play["XAxis"], play["YAxis"]), "TIPOFF")
    embed.add_field(name="Court", value=f"```text\n{court}\n```", inline=False)
    embed.set_thumbnail(url=embed_url)
    return embed


def Get_Basketball_Substitution_Embed(play, home_team, away_team, home_score, away_score, embed_url):
    # play["Substitutions"] holds every substitution row made at this stoppage, for both teams
    rows = play["Substitutions"]
    quarter = play["Quarter"]
    quarter_label = f"Q{quarter}" if quarter <= 4 else f"OT{quarter - 4}"

    embed = discord.Embed(
        colour=_bb_colour(play["Event"], play["Outcome"]),
        description=f"**{home_team} {home_score} - {away_team} {away_score}**",
        title=f"Play {play['PlayNumber']}: Substitution",
    )
    embed.add_field(name="Period", value=quarter_label, inline=True)
    embed.add_field(name="Game Clock", value=play["TimeOnClock"], inline=True)
    embed.add_field(name="Shot Clock", value=str(play["ShotClock"]), inline=True)

    team_ids = sorted({row["TeamID"] for row in rows}, key=lambda team_id: team_id != play["HomeTeamID"])
    teams = []
    for team_id in team_ids:
        team_rows = [row for row in rows if row["TeamID"] == team_id]
        fallback = home_team if team_id == play["HomeTeamID"] else away_team
        teams.append((team_rows[0].get("TeamAbbr") or fallback, team_rows))

    for direction, key in (("OUT", "SubstitutedPlayer"), ("IN", "SubstitutePlayer")):
        for abbr, team_rows in teams:
            names = [row.get(key) for row in team_rows if row.get(key)]
            embed.add_field(name=f"{abbr} {direction}:", value="\n".join(names) or "Not recorded", inline=True)
        for _ in range(3 - len(teams)):
            embed.add_field(name="\u200b", value="\u200b", inline=True)

    embed.set_thumbnail(url=embed_url)
    return embed


def Get_Basketball_Play_Delay(play):
    event = play["Event"]
    if event in ("Tipoff", "Ot_tipoff", "QuarterOver", "HalfOver", "GameOver", "OvertimeStart", "OvertimeOver"):
        return 6
    if event in _BB_SHOT_EVENTS or event == "Timeout":
        return 4
    return 2


_BB_ROUTINE_OUTCOMES = {"Move_success", "Pass_success"}
_BB_SKIPPED_OUTCOMES = {"Move_cutoff", "No_passing_lane"}


def _bb_is_routine(play):
    return play["Outcome"] in _BB_ROUTINE_OUTCOMES


def _bb_in_backcourt(play, home_team_id):
    # Home attacks toward +x and away toward -x; the frontcourt starts at |x| >= 1
    if play["TeamID"] == home_team_id:
        return play["XAxis"] <= 0
    return play["XAxis"] >= 0


def Get_Basketball_Stream_Plays(plays, home_team_id):
    # Everything is streamed except cut-off moves, no-lane passes, inbounds, routine backcourt
    # moves/passes, and all but the last of a run of the same routine move/pass.
    # Back-to-back substitution rows at the same clock are merged into one play.
    candidates = [
        play for play in plays
        if play["Outcome"] not in _BB_SKIPPED_OUTCOMES
        and play["Event"] != "Inbound"
        and not (_bb_is_routine(play) and _bb_in_backcourt(play, home_team_id))
    ]
    stream_plays = []
    for idx, play in enumerate(candidates):
        if play["Event"] == "Substitution":
            last = stream_plays[-1] if stream_plays else None
            if (
                last is not None
                and last["Event"] == "Substitution"
                and last["Quarter"] == play["Quarter"]
                and last["TimeOnClock"] == play["TimeOnClock"]
            ):
                last["Substitutions"].append(play)
            else:
                stream_plays.append({**play, "Substitutions": [play]})
            continue
        next_play = candidates[idx + 1] if idx + 1 < len(candidates) else None
        if (
            next_play is not None
            and _bb_is_routine(play)
            and _bb_is_routine(next_play)
            and play["Event"] == next_play["Event"]
            and play["TeamID"] == next_play["TeamID"]
        ):
            continue
        stream_plays.append(play)
    return stream_plays
