from app.models.team import Team


class Match:
    def __init__(self, home_team: Team, away_team: Team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = 0
        self.away_goals = 0

        self.events = []

