# Game class for game info
class Game:
    def __init__(self, matchup: str, away_team: str, home_team: str, away_score: str, home_score: str):
        self.matchup = matchup
        self.away_team = away_team
        self.home_team = home_team
        self.away_score = away_score
        self.home_score = home_score

    # Update game score
    def update_score(self, away_score: str, home_score: str):
        self.away_score = away_score
        self.home_score = home_score

    # Display game score
    def display_game_score(self):
        print(f"{self.away_team}: {self.away_score}\n{self.home_team}: {self.home_score}\n")
