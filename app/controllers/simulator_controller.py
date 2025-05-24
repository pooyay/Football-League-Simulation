import random

from app.models.team import Team
from app.models.match import Match


def age_factor(age):
    if 24 <= age <= 29:
        return 1.0
    elif age < 24:
        return 0.8 + 0.2 * (age / 24)
    elif age > 29:
        return max(0.0, 1.0 - 0.1 * (age - 29))


def player_score(player):
    base = player.goals * 4 + player.assists * 3 + player.caps * 1
    return base * age_factor(player.age)


def calculate_team_strength(team: Team):
    if not team.players:
        return 0
    total_score = sum(player_score(p) for p in team.players)
    return total_score / len(team.players)


def form_factor(last_5_results):
    score_map = {'W': 3, 'D': 1, 'L': 0}
    total_points = sum(score_map[r] for r in last_5_results)
    return 0.8 + (total_points / 15) * 0.4


def final_team_strength(team):
    return calculate_team_strength(team) * form_factor(team.last_5_results)


def simulate_goals(attacking_strength, defending_strength):
    ratio = attacking_strength / (defending_strength + 1)
    expected_goals = ratio * random.uniform(0.5, 1.5)
    goals = int(expected_goals) if random.random() > 0.3 else int(expected_goals) + 1
    return max(goals, 0)


def match_simulator(match: Match):
    home_strength = final_team_strength(match.home_team)
    away_strength = final_team_strength(match.away_team)

    match.home_goals = simulate_goals(home_strength, away_strength)
    match.away_goals = simulate_goals(away_strength, home_strength)

    match.home_team.update_team_stat(match.home_goals, match.away_goals)
    match.away_team.update_team_stat(match.away_goals, match.home_goals)


    return match
