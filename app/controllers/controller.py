from app.controllers import data_controller
from app.controllers.team_controller import update_team_players

from app.views.cli_view import show_menu, get_user_command, show_teams, show_standings, unknown_command, get_team_name, \
    show_team_details


def controller():
    teams = data_controller.get_teams_from_file("input/teams.json")
    players = data_controller.get_players_from_file("input/players.json")
    update_team_players(players, teams)

    while True:
        show_menu()
        command = get_user_command()

        if command == "list":
            show_teams(teams)

        elif command == "show":
            name = get_team_name()
            team = next((t for t in teams if t.name.lower() == name.lower()), None)
            if team:
                show_team_details(team)
            else:
                print(f"Team '{name}' not found. Please try again.")

        elif command == "standings":
            show_standings(teams)

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            unknown_command()
