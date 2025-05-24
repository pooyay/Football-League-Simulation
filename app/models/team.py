class Team:
    def __init__(self, name: str, points: int = 0, wins: int = 0, draw: int = 0, losses: int = 0,
                 goals_scored: int = 0, goals_conceded: int = 0):
        self.name = name
        self.points = points
        self.wins = wins
        self.draw = draw
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_conceded = goals_conceded

        self.players = []
        self.last_5_results = []

    def update_team_stat(self, goals_for, goals_against):
        self.goals_scored += goals_for
        self.goals_conceded += goals_against
        if goals_for > goals_against:
            self.wins += 1
            self.points += 3
            result = 'W'
        elif goals_for == goals_against:
            self.draw += 1
            self.points += 1
            result = 'D'
        else:
            self.losses += 1
            result = 'L'

        self.last_5_results.append(result)
        if len(self.last_5_results) > 5:
            self.last_5_results.pop(0)

    def add_player(self, player):
        self.players.append(player)

    def __repr__(self):
        return f"<Team {self.name} with {len(self.players)} players>"
