# Get scores from ESPN API

import requests
from jsonpath_ng import parse
from game import Game

# Parse scoreboard and return a list of events using event class
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
    # Away = competitors[0]
    # Home = competitors[1]

    jsonpath_expression = parse(f'$.events[*].competitions[0].competitors[0].team.abbreviation')

    for match in jsonpath_expression.find(json_string):
        home_team.append(match.value)

    jsonpath_expression = parse(f'$.events[*].competitions[0].competitors[1].team.abbreviation')
    
    for match in jsonpath_expression.find(json_string):
        away_team.append(match.value)

    # Get scores
    # Away = scores[0]
    # Home = scores[1]

    jsonpath_expression = parse(f'$.events[*].competitions[0].competitors[0].score')

    for match in jsonpath_expression.find(json_string):
        home_score.append(match.value)

    jsonpath_expression = parse(f'$.events[*].competitions[0].competitors[1].score')
        
    for match in jsonpath_expression.find(json_string):
        away_score.append(match.value)
    
    # Display for debugging purposes
    for i in range(len(matchups)):
       games.append(Game(matchups[i], away_team[i], home_team[i], away_score[i], home_score[i]))

    return games

# ---------------------------------------- #

def main():
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
        for game in games:
            game.display_game_score()
    else:
        print(f"Failed. Status code: {response.status_code}")

if __name__ == "__main__":
    main()