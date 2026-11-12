# Get scores from ESPN API

import requests
from jsonpath_ng import parse
from game import Game
from flask import Flask, render_template

# Parse scoreboard and return a list of events using event class
# TODO: clean up this function. It's ugly!

def parse_scoreboard(json_string: str) -> list:

    # Define lists
    games = []
    matchups = []
    away_team = []
    home_team = []
    away_score = []
    home_score = []

    # Get info for Event class objects
    jsonpath_expression = parse('$.events[*].name')

    for match in jsonpath_expression.find(json_string):
        matchups.append(match.value)

    # Get teams
    # Home = competitors[0]
    # Away = competitors[1]

    jsonpath_expression = parse(f'$.events[*].competitions[0].competitors[0].team.abbreviation')

    for match in jsonpath_expression.find(json_string):
        home_team.append(match.value)

    jsonpath_expression = parse(f'$.events[*].competitions[0].competitors[1].team.abbreviation')
    
    for match in jsonpath_expression.find(json_string):
        away_team.append(match.value)

    # Get scores
    # Home = scores[0]
    # Away = scores[1]

    jsonpath_expression = parse(f'$.events[*].competitions[0].competitors[0].score')

    for match in jsonpath_expression.find(json_string):
        home_score.append(match.value)

    jsonpath_expression = parse(f'$.events[*].competitions[0].competitors[1].score')
        
    for match in jsonpath_expression.find(json_string):
        away_score.append(match.value)
    
    # Instantiate new Game using values retrieved above
    for i in range(len(matchups)):
       games.append(Game(i, matchups[i], away_team[i], home_team[i], away_score[i], home_score[i]))

    return games

# ---------------------------------------- #


# API endpoint
# Put this in an environment variable instead? Probably doesn't matter
url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

# Send request
response = requests.get(url)

# Do stuff
# This kind of sucks. Try/except?
if response.status_code == 200:
    data = response.json()
    games = parse_scoreboard(data)
else:
    print(f"Failed. Status code: {response.status_code}")

# ---------------------------------------- #

matchups = []
for game in games:
    matchups.append(game.get_matchup())

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('scoreboard.html', matchups=matchups)

if __name__ == "__main__":
    app.run()