import unittest
import random

from app.models.player import Player
from app.models.team import Team
from app.models.match import Match

from app.controllers.simulator_controller import (
    age_factor, player_score, calculate_team_strength,
    form_factor, final_team_strength,
    simulate_goals, match_simulator
)


def create_player(age, goals, assists, caps):
    return Player(name="Test Player", age=age, position=["Midfielder"],
                  team="Test Team", number="10",
                  goals=goals, assists=assists, caps=caps)


def create_team(players=None, last_5_results=None):
    t = Team(name="Test Team")
    t.players = players or []
    t.last_5_results = last_5_results or []
    t.points = 0
    t.wins = 0
    t.draws = 0
    t.losses = 0
    t.goals_scored = 0
    t.goals_conceded = 0
    return t


class TestMatchSimulator(unittest.TestCase):

    def test_age_factor_peak_and_decline(self):
        self.assertEqual(age_factor(25), 1.0)
        self.assertEqual(age_factor(24), 1.0)
        self.assertEqual(age_factor(29), 1.0)
        self.assertGreater(age_factor(20), 0.8)
        self.assertLess(age_factor(20), 1.0)
        self.assertLess(age_factor(35), 1.0)
        self.assertGreaterEqual(age_factor(40), 0.0)

    def test_player_score_varies_with_stats_and_age(self):
        young = create_player(20, 5, 3, 10)
        peak = create_player(25, 5, 3, 10)
        old = create_player(35, 5, 3, 10)
        score_young = player_score(young)
        score_peak = player_score(peak)
        score_old = player_score(old)
        self.assertGreaterEqual(score_peak, score_young)
        self.assertGreaterEqual(score_peak, score_old)

    def test_calculate_team_strength_average(self):
        p1 = create_player(25, 10, 5, 20)
        p2 = create_player(25, 5, 2, 10)
        team = create_team(players=[p1, p2])
        strength = calculate_team_strength(team)
        expected = (player_score(p1) + player_score(p2)) / 2
        self.assertAlmostEqual(strength, expected)

    def test_form_factor_extremes(self):
        self.assertAlmostEqual(form_factor(['W', 'W', 'W', 'W', 'W']), 1.2)
        self.assertAlmostEqual(form_factor(['L', 'L', 'L', 'L', 'L']), 0.8)
        mixed = form_factor(['W', 'D', 'L', 'W', 'D'])
        self.assertTrue(0.8 < mixed < 1.2)

    def test_final_team_strength_combines_factors(self):
        p = create_player(25, 10, 5, 20)
        team = create_team(players=[p], last_5_results=['W', 'W', 'D', 'L', 'W'])
        strength = final_team_strength(team)
        base = calculate_team_strength(team)
        form = form_factor(team.last_5_results)
        self.assertAlmostEqual(strength, base * form)

    def test_simulate_goals_output(self):
        random.seed(42)
        goals = simulate_goals(100, 50)
        self.assertIsInstance(goals, int)
        self.assertGreaterEqual(goals, 0)

    def test_update_team_stats_correctly_updates(self):
        team = create_team()
        team.update_team_stat(2,1)
        self.assertEqual(team.wins, 1)
        self.assertEqual(team.points, 3)
        self.assertEqual(team.goals_scored, 2)
        self.assertEqual(team.goals_conceded, 1)
        self.assertEqual(team.last_5_results[-1], 'W')

        team.update_team_stat(1,1)
        self.assertEqual(team.draw, 1)
        self.assertEqual(team.points, 4)
        self.assertEqual(team.last_5_results[-1], 'D')

        team.update_team_stat(0,2)
        self.assertEqual(team.losses, 1)
        self.assertEqual(team.points, 4)
        self.assertEqual(team.last_5_results[-1], 'L')

    def test_match_simulator_simulates_and_updates_stats(self):
        p1 = create_player(25, 10, 5, 20)
        p2 = create_player(28, 8, 4, 15)
        home_team = create_team(players=[p1], last_5_results=['W', 'W', 'D', 'L', 'W'])
        away_team = create_team(players=[p2], last_5_results=['L', 'D', 'L', 'W', 'D'])

        match = Match(home_team, away_team)
        match_simulator(match)

        self.assertIsInstance(match.home_goals, int)
        self.assertGreaterEqual(match.home_goals, 0)
        self.assertIsInstance(match.away_goals, int)
        self.assertGreaterEqual(match.away_goals, 0)

        # update_team_stats(home_team, result.home_goals, result.away_goals)
        # update_team_stats(away_team, result.away_goals, result.home_goals)

        self.assertLessEqual(len(home_team.last_5_results), 5)
        self.assertLessEqual(len(away_team.last_5_results), 5)


if __name__ == "__main__":
    unittest.main()
