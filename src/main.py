# Get scores from ESPN API

import requests
# import json
from jsonpath_ng import parse

# Event class for game info
class Event:
    def __init__(self, event: str, away_team: str, home_team: str, away_score: str, home_score: str):
        self.event = event
        self.away_team = away_team
        self.home_team = home_team
        self.away_score = away_score
        self.home_score = home_score

    def update_score(self, away_score: str, home_score: str):
        self.away_score = away_score
        self.home_score = home_score

# Parse scoreboard and return a list of events using event class
def parse_scoreboard(json_string: str) -> list:

    # Define variables
    event = ""
    away_team = ""
    home_team = ""
    away_score = ""
    home_score = ""

    # Define JSON paths
    
    # Get event name (Away at Home), then display all events
    jsonpath_expression = parse('$.events[*].name')

    for match in jsonpath_expression.find(json_string):
            print(match.value)

    # Get scores
    # Away = scores[0]
    # Home = scores[1]
    
    jsonpath_expression = parse('$.events[*].competitions[0].competitors[0].score[0]')
    for match in jsonpath_expression.find(json_string):
         print(match.value)

    # return parsed_data

# Get all scores, return dictionary? 
# { Game : Score0 to Score1 }
def get_events(url: str):

    # Send request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        parse_scoreboard(data)
    else:
        print(f"Failed. Status code: {response.status_code}")

   #  return game_scores

# API endpoint
url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

get_events(url)