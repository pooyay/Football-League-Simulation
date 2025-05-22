from app.controllers import data_controller


def controller():
    teams = data_controller.get_teams_from_file("input/teams.json")
    players = data_controller.get_players_from_file("input/players.json")
    teams_dict = {
        team.name: team
        for team in teams
    }
    for player in players:
        teams_dict[player.team_name].add_player(player)
    for team in teams:
        print(team)

