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

    def update_team_stat(self, points: int = 0, wins: int = 0, draw: int = 0, losses: int = 0,
                         goals_scored: int = 0, goals_conceded: int = 0):
        self.points = points
        self.wins = wins
        self.draw = draw
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_conceded = goals_conceded

    def add_player(self, player):
        self.players.append(player)

    # def __str__(self):
    #     return self.name

    def __repr__(self):
        # return f"<{self.name} - {self.points} points>"
        return f"<Team {self.name} with {len(self.players)} players>"
