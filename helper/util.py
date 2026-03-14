import random

def IsPenalty(res: str):
    sub_str = res[0:7]
    return sub_str == "PENALTY"

def IsInjury(res: str):
    sub_str = res[0:6]
    return sub_str == "INJURY"

def IsRedzone(res: str):
    sub_str = res[0:7]
    return sub_str == "REDZONE"

def GetIntroPenaltyStr():
    intro_list = [
        "It looks like there's a flag on the field! Let's see what the refs have to say...",
        "And there's a flag on the field! Refs spotted something that didn't seem right...",
        "And a flag is thrown onto the field! Refs caught something on the play...",
        "Refs are whistling and a flag has been thrown onto the field. Let's see what they have to say..."
    ]

    return random.choice(intro_list)

def PickBKAnnouncer():
    base_list = ['BK Toucan', 'DJ Byeson', 'Kenny', 'Jody', 'Madison', 'Ian', 'Joshua']
    return random.choice(base_list)

def PickHKAnnouncer():
    base_list = ['HK Toucan', 'HK Dante', 'Penny', 'Maurice']
    return random.choice(base_list)

def PickAnnouncer(league: str, home_id):
    # Specific Announcer Requests
    if home_id == 32 and league != 'nfl':
        return 'Mad Dog Howard'
    elif (home_id == 9 or home_id == 182 or home_id == 1) and league != 'nfl':
        return 'Captain Jonas'
    elif (home_id == 118 and league != 'nfl'):
        return 'Sage Bow'
    elif (home_id == 44 and league != 'nfl'):
        return 'Versace'
    elif (home_id == 67 and league != 'nfl'):
        return 'Corn'
    elif (home_id == 128 and league != 'nfl'):
        return 'Jack Stallions'
    elif (home_id == 129 and league != 'nfl'):
        return 'Matt Payme'
    elif (home_id == 90 and league != 'nfl'):
        return 'MrManul'
    base_list = []
    if league != 'nfl':
        base_list += ['Phil Mattenborough', 'Dante the Bison', 'Craig Newton', 'Holly Park', 'Toucan', 'J-M-988']
    else:
        # Random number between 1 and 100, if 100, return Slippery Jim
        rand_num = random.randrange(1,101)
        if rand_num >= 100:
            return 'Slippery Jim'
        base_list += ['Leftenant Amy Cross', 'Terry Ross', 'AK-T-Y4M4', 'Bill Kirksby', 'Toucan', 'Captain Jonas']

    return random.choice(base_list)

def BKAnnouncerIntroText(announcer: str, ht: str, at: str, league: str, stadium: str):
    league_str = "SimCBB"
    if league == 'nba':
        league_str = "SimNBA"
    announcer_intro_book = {
      'BK Toucan': f"Hello and welcome to another exciting broadcast of the {league_str} show! I am your host, ToucanSoda, and today I will be covering the {ht} and the {at} in this very exciting matchup here at {stadium}!",
      "Joshua": f"What's up everybody, welcome another {league_str} matchup at {stadium}! I am your host, Joshua Pilot, and today I will be covering the {ht} and the {at}!",
      "DJ Byeson": f"Yo what's up and welcome to another exciting matchup of the {league_str} show! I am your host, DJ Bye-Son, and today I will be covering the {ht} and the {at} in this very exciting matchup here at {stadium}!",
      "Kenny": f"Hey there, welcome to another exciting matchup of the {league_str} show! I am your host, Kenny Bobcat, and today I will be covering the {ht} and the {at} in this very exciting matchup here at {stadium}!",
      "Jody": f"Helloooooo basketball fans! Welcome to another exciting matchup of the {league_str} show! I am your host, Jody Hoya, and today I will be covering the {ht} and the {at} in this very exciting matchup here at {stadium}!",
      "Madison": f"Welcome fans and all another exciting matchup of the {league_str} show! I am your host, Madison Gardner, and today I will be covering the {ht} and the {at} in this very exciting matchup here at {stadium}!",
      "Ian": f"Fellow patriots, WELCOME to another exciting matchup of the {league_str} show! I am your host, Ian the Eagle, and today I will be covering the {ht} and the {at} in this very patriotic matchup here at {stadium}!",
    }
    return announcer_intro_book[announcer]

def HKAnnouncerIntroText(announcer: str, ht: str, at: str, league: str, arena: str):
    league_str = "SimCHL"
    if league == 'phl':
        league_str = "SimPHL"
    announcer_intro_book = {
      'HK Toucan': f"Hello and welcome to another exciting broadcast of the {league_str} show! I am your host, ToucanSoda, and today I will be covering the {ht} and the {at} in this very exciting matchup here at {arena}!",
      "Penny": f"What's up everybody, welcome to another {league_str} matchup at {arena}! I am your host, Penny, and today I will be covering the {ht} and the {at}!",
      "HK Dante": f"Yo what's up and welcome to another exciting matchup of the {league_str} show! Dante the Bison here once again, and today I will be covering the {ht} and the {at} in this very exciting matchup here at {arena}!",
      "Maurice": f"Hey there, welcome to another exciting matchup of the {league_str} show! I am your host, Maurice the Moose, and today I will be covering the {ht} and the {at} in this very exciting matchup here at {arena}!",
    }
    return announcer_intro_book[announcer]


def AnnouncerIntroText(announcer: str, ht: str, at: str, league: str, stadium: str):
    league_str = "SimCFB"
    if league == 'nfl':
        league_str = "SimNFL"
    announcer_intro_book = {
    'AK-T-Y4M4': f"Greetings humans and welcome to another exciting game of American Sport: Football! I am your host, AK-T-Y4M4, and I will be vocally reporting today's matchup! ",
    'Bill Kirksby':f"Hellooooo and welcome {league_str} fans! Welcome to another exciting matchup between the {ht} and the {at}!",
    'Bread Man':f"Hello fans! Welcome to today's exciting {league_str} matchup between the {ht} and the {at}! I am your host for today's game, Bread Man!",
    'Captain Jonas': f"Attention and welcome fans! I am your host for today's {league_str} match up, Captain Jonas. Today's matchup is between the {ht} and the {at}. Please be seated accordingly and pay attention to the game.",
    'Craig Newton': f"Hello college sports fans! Craig Newton here, welcoming you to another exciting {league_str} matchup! Tonights game features the {ht} and the {at}",
    'Dante the Bison': f"Hello, hello fans! Welcome to another wonderful day of {league_str} football! I am your lucky and humble host, Dante the Bison, here to report to you today's matchup between the {ht} and the {at}. Grab your snacks and get ready! I think this game is an exciting one.",
    'Holly Park': f"Yoo-Hoo! Hello football fans! I am Holly Park, your faithful announcer streaming from Goyang, South Korea tonight's {league_str} football game! Today, we have an exhilarating matchup between the {ht} and the {at}. Tune in and grab your buddies, this is a good one!",
    'J-M-988': f"REPORTING: Hello avid fans. Welcome to today's simulated {league_str} matchup between the {ht} and the {at}. I am your host, J-M-988. I have the intel for this simulation, which I have confirmed is - fascinating. I will provide you the intel and play by play in a dedicated format readable and translated for your viewing. Loading now...",
    'Leftenant Amy Cross': f"Hello sports fans! Leftenant Amy Cross reporting in, here to welcome you to today's exciting {league_str} game between the {ht} and the {at}. I hope you're ready, because I certainly am looking forward to reporting this game for you!",
    'Phil Mattenborough': f"Welcome fellow {league_str} fans! Phil Mattenborough here in {stadium} to broadcast today's game between the {ht} and the {at}, just for you. Grab a seat and listen in folks, because this is one matchup I've been looking forward to!",
    'Slippery Jim': f"Good evening, {league_str} faithful... or should I say, *unfortunate witnesses.* This is your new play-by-play man— the illustrious, the infamous, the *utterly untouchable* Slippery Jim! Tonight’s broadcast of the {ht} versus the {at} is under *my* command. The doors are locked, the mics are hot, and the truth? Well… it’s whatever I say it is. Sit tight, keep those eyes on the field, and remember — every call I make changes the game. Let’s play, shall we?",
    'Terry Ross': f"Hello and welcome to another {league_str} broadcast, hosted by your's truly -- Terry Ross. Today's matchup is between the {ht} and the {at} here in {stadium}.",
    'Toucan': f"Hello and welcome to another exciting broadcast of the {league_str} show! I am your host, ToucanSoda, and today I will be covering the {ht} and the {at} in this very exciting matchup here in {stadium}!",
    'Mad Dog Howard': f"Hello Seminoles fans! 'Mad Dog' Howard live here in {stadium} to report to you another exicing matchup between the {ht} and the {at}!",
    'Sage Bow': f" GET UP UTE NATION. UTE THUNDER IS PRIMED AND READY TO FIRE. THE MUSS IS ON THEIR FEET. Who am I, sir? A Utah Man am I. A Utah Man, sir, and will be ’til I die; Ki-yi!",
    'Corn': "Corn. Oh, and uh... go huskers.",
    'Jack Stallions': "Hello world. We are LIVE, watching some of the finest young men in the world galloping on God's green earth!  I'm Jack Stallions, join me in celebrating Broncos' football.",
    'Matt Payme':"Good afternoon from Barry Alvarez Field at Camp Randall Stadium. Alongside Marv Talksnotmuch and our sideline reporter, Larry Getback, this is Matt Payme. We welcome you to Wisconsin. And remember, it never snows in Camp Randall Stadium.",
    'MrManul':"Hello Spartan nation. This is your favorite cat Mr. Manul and welcome to another exciting week of San José football!",
    'Versace':"Hunghhh... It's Versace... It's a beautiful day outside today, gonna tell you all about some football plays, we've got the Jayhawks out of Kansas, gonna call Rock Chalk with both eyes closed. Brrrrrrrrr!"
    }
    return announcer_intro_book[announcer]

def GetHockeyLetterGrade(attr, year):
    if year < 3:
        if attr > 18:
            return "A"
        if attr > 12:
            return "B"
        if attr > 7:
            return "C"
        if attr > 4:
            return "D"
        return "F"
    if attr > 24:
        return "A+"
    if attr > 21:
        return "A"
    if attr > 18:
        return "A-"
    if attr > 16:
        return "B+"
    if attr > 14:
        return "B"
    if attr > 12:
        return "B-"
    if attr > 10:
        return "C+"
    if attr > 8:
        return "C"
    if attr > 6:
        return "C-"
    if attr > 4:
        return "D"
    return "F"

def GetYear(year: int, is_redshirt: bool):
    open = ""
    close = ""
    if is_redshirt:
        year = year-1
        open = "("
        close = ")"
    if year == 1:
        return f"{open}Fr{close}"
    elif year == 2:
        return f"{open}So{close}"
    elif year == 3:
        return f"{open}Jr{close}"
    elif year == 4:
        return f"{open}Sr{close}"
    elif year == 5:
        return f"{open}Gr{close}"
    return f"{open}{year}{close}"