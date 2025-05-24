import unittest
from app.models.team import Team
from app.models.player import Player


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("Champions")

    def test_team_creation_defaults(self):
        self.assertEqual(self.team.name, "Champions")
        self.assertEqual(self.team.points, 0)
        self.assertEqual(self.team.wins, 0)
        self.assertEqual(self.team.draw, 0)
        self.assertEqual(self.team.losses, 0)
        self.assertEqual(self.team.goals_scored, 0)
        self.assertEqual(self.team.goals_conceded, 0)
        self.assertEqual(len(self.team.players), 0)

    def test_add_player(self):
        player = Player("Jane", 22, ["Forward"], "Champions", "9", 3, 4, 5)
        self.team.add_player(player)
        self.assertIn(player, self.team.players)
        self.assertEqual(len(self.team.players), 1)

    def test_repr(self):
        self.assertEqual(repr(self.team), "<Team Champions with 0 players>")
        player = Player("Jane", 22, ["Forward"], "Champions", "9", 3, 4, 5)
        self.team.add_player(player)
        self.assertEqual(repr(self.team), "<Team Champions with 1 players>")

    def test_update_team_stat(self):
        self.team.update_team_stat(points=12, wins=7, draw=3, losses=2, goals_scored=20, goals_conceded=10)
        self.assertEqual(self.team.points, 12)
        self.assertEqual(self.team.wins, 7)
        self.assertEqual(self.team.draw, 3)
        self.assertEqual(self.team.losses, 2)
        self.assertEqual(self.team.goals_scored, 20)
        self.assertEqual(self.team.goals_conceded, 10)


if __name__ == "__main__":
    unittest.main()
