def show_welcome():
    print("/////////////////////////////////////////////////")
    print("//  Welcome to the Football League Simulator!  //")
    print("/////////////////////////////////////////////////")


def show_teams(teams: list):
    sorted_teams = sorted(teams, key=lambda t: t.name)
    print("\nTeams:")
    for team in sorted_teams:
        print(f"- {team.name}")
    print()


def show_team_details(team):
    print(f"\nTeam: {team.name}")
    print(f"Points: {team.points}")
    print(f"Goals Scored: {team.goals_scored}")
    print(f"Goals Conceded: {team.goals_conceded}")
    print("Players:")
    for player in team.players:
        print(f" - {player.name} ({player.position})")


def show_standings(teams):
    print("\n📊 League Standings:")
    sorted_teams = sorted(teams, key=lambda t: (-t.points, -t.goals_scored, t.goals_conceded, t.name))
    for index, team in enumerate(sorted_teams, start=1):
        print(
            f"{index}. {team.name:20} | Points: {team.points:2} | "
            f"GF: {team.goals_scored:2} | GA: {team.goals_conceded:2}"
        )


def show_menu():
    print("\nAvailable Commands:")
    print("  list       - Show all teams")
    print("  show       - Show details for a specific team")
    print("  simulate   - Simulate the full league")
    print("  standings  - Show current standings")
    print("  exit       - Exit the program")


def get_user_command():
    return input("\nEnter command: ").strip().lower()


def get_team_name():
    return input("Enter the team name: ").strip()


def unknown_command():
    print("Unknown command. Please try again.")
