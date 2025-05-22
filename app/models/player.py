from app.models.team import Team


class Player:
    def __init__(self, name: str, age: int, position: list, team: str, number: str,
                 goals: int, assists: int, caps: int):
        self.name = name
        self.age = age
        self.position = position
        self.team_name = team
        self.number = number

        self.goals = goals
        self.assists = assists
        self.caps = caps

        self.team: Team or None = None

    def __repr__(self):
        return f"<Player {self.name}, Team: {self.team.name if self.team else 'None'}>"
