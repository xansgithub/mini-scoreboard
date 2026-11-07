# Get scores from ESPN API
# $.events[14].competitions[0].competitors[0].score

import requests

# API endpoint
url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

# Send request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed. Status code: {response.status_code}")