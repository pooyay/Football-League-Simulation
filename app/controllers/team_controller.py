from app.models.player import Player
from app.models.team import Team


def update_team_players(players: list[Player], teams: list[Team]):
    teams_dict = {
        team.name: team
        for team in teams
    }
    for player in players:
        teams_dict[player.team_name].add_player(player)
