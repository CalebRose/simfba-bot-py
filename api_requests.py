import requests
import json

fba_url = "https://simfba.azurewebsites.net/api/"
test_url = "http://localhost:5001/api/"
bba_test_url = "http://localhost:8081/api/"
bba_url = "https://simnba.azurewebsites.net/api/"
hck_test_url = "http://localhost:8080/api/"
hck_url = "https://simhck-hqd2bme9gse5d7g9.westus-01.azurewebsites.net/api/"
# bba_url = bba_test_url

def GetCollegeBasketballTeam(id):
    res = requests.get(f"{bba_url}ds/cbb/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballPlayer(first_name, last_name, id):
    res = requests.get(f"{bba_url}ds/cbb/player/name/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballPlayer_id(id):
    res = requests.get(f"{bba_url}ds/cbb/player/id/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNBABasketballPlayer_id(id):
    res = requests.get(f"{bba_url}ds/nba/player/id/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNBABasketballTeam(id):
    res = requests.get(f"{bba_url}ds/nba/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNBABasketballPlayer(first_name, last_name, id):
    res = requests.get(f"{bba_url}ds/nba/player/name/{first_name}/{last_name}/{id}")
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

def GetCollegeFootballCrootName(first_name, last_name):
    res = requests.get(f"{fba_url}ds/cfb/croot/name/{first_name}/{last_name}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballCrootingClass(id):
    res = requests.get(f"{fba_url}ds/cfb/croots/class/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballCroot(id):
    res = requests.get(f"{bba_url}ds/cbb/croot/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballCrootName(first_name, last_name):
    res = requests.get(f"{bba_url}ds/cbb/croot/name/{first_name}/{last_name}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballCrootingClass(id):
    res = requests.get(f"{bba_url}ds/cbb/croots/class/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballConfStandings(id):
    res = requests.get(f"{fba_url}ds/cfb/conference/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballConfStandings(id):
    res = requests.get(f"{bba_url}ds/cbb/conf/standings/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNBABasketballConfStandings(id):
    res = requests.get(f"{bba_url}ds/nba/conf/standings/{id}")
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

def StreamFootballGames(league, timeslot, isNFL):
    req_url = ""
    if isNFL == False:
        req_url = f"{fba_url}ds/cfb/{league}/stream/{timeslot}/"
    else:
        req_url = f"{fba_url}ds/nfl/league/stream/{timeslot}/"
    res = requests.get(f"{req_url}")
    if res.status_code == 200:
        return res.json()
    return False

def StreamHockeyGames(isPro, streamType):
    req_url = ""
    if isPro == False:
        req_url = f"{hck_url}ds/chl/stream/{streamType}/"
    else:
        req_url = f"{hck_url}ds/phl/stream/{streamType}/"
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
        req_url = f"{bba_url}ds/cbb/assign/discord/{team_id}/{user}"
    else:
        req_url = f"{bba_url}ds/nba/assign/discord/{team_id}/{user}/{username}"
    res = requests.get(f"{req_url}")
    if res.status_code == 200:
        return True
    return False

def RegisterHCTeam(isPHL, team_id, user):
    req_url = ""
    if isPHL == False:
        req_url = f"{hck_url}ds/chl/assign/discord/{team_id}/{user}"
    else:
        req_url = f"{hck_url}ds/phl/assign/discord/{team_id}/{user}"
    res = requests.get(f"{req_url}")
    if res.status_code == 200:
        return True
    return False

def CompareTwoCHLTeams(t1, t2):
    res = requests.get(f"{hck_url}ds/chl/flex/{t1}/{t2}")
    if res.status_code == 200:
        return res.json()
    return False

def CompareTwoPHLTeams(t1, t2):
    res = requests.get(f"{hck_url}ds/phl/flex/{t1}/{t2}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeHockeyTeam(id):
    res = requests.get(f"{hck_url}ds/chl/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetPHLHockeyTeam(id):
    res = requests.get(f"{hck_url}ds/phl/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeHockeyPlayer(first_name, last_name, id):
    res = requests.get(f"{hck_url}ds/chl/player/name/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeHockeyPlayer_id(id):
    res = requests.get(f"{hck_url}ds/chl/player/id/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetPHLHockeyPlayer(first_name, last_name, id):
    res = requests.get(f"{hck_url}ds/phl/player/name/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetPHLHockeyPlayer_id(id):
    res = requests.get(f"{hck_url}ds/phl/player/id/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeHockeyCroot(id):
    res = requests.get(f"{hck_url}ds/chl/croot/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeHockeyCrootingClass(id):
    res = requests.get(f"{hck_url}ds/chl/croots/class/{id}")
    if res.status_code == 200:
        return res.json()
    return False
