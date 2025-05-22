import json

from app.models.team import Team
from app.models.player import Player


def get_teams_from_file(filename: str) -> list[Team]:
    with open(filename, 'r') as file:
        data = json.load(file)

    teams = [Team(**team_dict) for team_dict in data]
    return teams


def get_players_from_file(filename: str) -> list:
    with open(filename, 'r') as file:
        data = json.load(file)

    players = [Player(**player_dict) for player_dict in data]
    return players
