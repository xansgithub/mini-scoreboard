# Game class for game info
class Game:
    def __init__(self, id: int, matchup: str, away_team: str, home_team: str, away_score: str, home_score: str):
        self.id = id
        self.matchup = matchup
        self.away_team = away_team
        self.home_team = home_team
        self.away_score = away_score
        self.home_score = home_score

    # Display game score
    def get_matchup(self):
        return f"{self.away_team}: {self.away_score} {self.home_team}: {self.home_score}"