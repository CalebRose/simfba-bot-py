import requests
import json

fba_url = "https://simfba.azurewebsites.net/api/"
test_url = "http://localhost:5001/api/"
bba_test_url = "http://localhost:8081/api/"
bba_url = "https://simnba.azurewebsites.net/api/"
# bba_url = bba_test_url

def GetCollegeBasketballTeam(id):
    res = requests.get(f"{bba_url}dis/cbb/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballPlayer(first_name, last_name, id):
    res = requests.get(f"{bba_url}dis/cbb/player/name/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballPlayer_id(id):
    res = requests.get(f"{bba_url}dis/cbb/player/id/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNBABasketballPlayer_id(id):
    res = requests.get(f"{bba_url}dis/nba/player/id/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNBABasketballTeam(id):
    res = requests.get(f"{bba_url}dis/nba/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNBABasketballPlayer(first_name, last_name, id):
    res = requests.get(f"{bba_url}dis/nba/player/name/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def CompareTwoNBATeams(t1, t2):
    res = requests.get(f"{bba_url}ds/nba/flex/{t1}/{t2}")
    if res.status_code == 200:
        return res.json()
    return False

def GetAllCBBMatches():
    res = requests.get(f"{bba_url}match/season/3")
    if res.status_code == 200:
        return res.json()
    return False

def CompareTwoCBBTeams(t1, t2):
    res = requests.get(f"{bba_url}ds/cbb/flex/{t1}/{t2}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballPlayer(first_name, last_name, id):
    res = requests.get(f"{fba_url}ds/cfb/player/name/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballPlayer_id(id):
    res = requests.get(f"{fba_url}ds/cfb/player/id/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballPlayerCareer_id(id):
    res = requests.get(f"{fba_url}ds/college/player/careerstats/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNFLFootballPlayer(first_name, last_name, id):
    res = requests.get(f"{fba_url}ds/nfl/player/name/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNFLFootballPlayer_id(id):
    res = requests.get(f"{fba_url}ds/nfl/player/id/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNFLFootballPlayerCareer_id(id):
    res = requests.get(f"{fba_url}ds/nfl/player/careerstats/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballPlayerIndStats(first_name, last_name, id, week):
    res = requests.get(f"{fba_url}ds/cfb/player/indstats/{first_name}/{last_name}/{id}/{week}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballPlayerSeasonStats(first_name, last_name, id):
    res = requests.get(f"{fba_url}ds/cfb/player/seasonsstats/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballCroot(id):
    res = requests.get(f"{fba_url}ds/cfb/croot/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballCrootingClass(id):
    res = requests.get(f"{fba_url}ds/cfb/croots/class/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballConfStandings(id):
    res = requests.get(f"{fba_url}ds/cfb/conference/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballTeam(id):
    res = requests.get(f"{fba_url}ds/cfb/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def CompareTwoCFBTeams(t1, t2):
    res = requests.get(f"{fba_url}ds/cfb/flex/{t1}/{t2}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNFLFootballConfStandings(id):
    res = requests.get(f"{fba_url}ds/nfl/conference/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNFLFootballDiviStandings(id):
    res = requests.get(f"{fba_url}ds/nfl/division/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNFLFootballTeam(id):
    res = requests.get(f"{fba_url}teams/nfl/roster/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def CompareTwoNFLTeams(t1, t2):
    res = requests.get(f"{fba_url}ds/nfl/flex/{t1}/{t2}")
    if res.status_code == 200:
        return res.json()
    return False

def StreamFootballGames(league, timeslot, week, isNFL):
    req_url = ""
    if isNFL == False:
        req_url = f"{fba_url}ds/cfb/{league}/stream/{timeslot}/{week}/"
    else:
        req_url = f"{fba_url}ds/nfl/league/stream/{timeslot}/{week}/"
    res = requests.get(f"{req_url}")
    if res.status_code == 200:
        return res.json()
    return False

def RegisterFBTeam(isNFL, team_id, user):
    req_url = ""
    if isNFL == False:
        req_url = f"{fba_url}ds/cfb/assign/discord/{team_id}/{user}"
    else:
        req_url = f"{fba_url}ds/nfl/assign/discord/{team_id}/{user}"
    res = requests.get(f"{req_url}")
    if res.status_code == 200:
        return True
    return False

def RegisterBBTeam(isNBA, team_id, user, username):
    req_url = ""
    if isNBA == False:
        req_url = f"{bba_url}ds/cbb/assign/discord/{team_id}/{user}/{username}"
    else:
        req_url = f"{bba_url}ds/nba/assign/discord/{team_id}/{user}/{username}"
    res = requests.get(f"{req_url}")
    if res.status_code == 200:
        return True
    return False
