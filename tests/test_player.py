import unittest

from app.models.player import Player
from app.models.team import Team


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.team = Team("Testers")
        self.player = Player(
            name="John Doe",
            age=25,
            position=["Midfielder"],
            team=self.team.name,
            number="10",
            goals=5,
            assists=7,
            caps=12
        )
        self.player.team = self.team  # assign the team object

    def test_player_creation(self):
        self.assertEqual(self.player.name, "John Doe")
        self.assertEqual(self.player.age, 25)
        self.assertEqual(self.player.position, ["Midfielder"])
        self.assertEqual(self.player.team_name, "Testers")
        self.assertEqual(self.player.number, "10")
        self.assertEqual(self.player.goals, 5)
        self.assertEqual(self.player.assists, 7)
        self.assertEqual(self.player.caps, 12)
        self.assertIs(self.player.team, self.team)

    def test_repr(self):
        expected = "<Player John Doe, Team: Testers>"
        self.assertEqual(repr(self.player), expected)

        # Test repr when no team assigned
        self.player.team = None
        expected_no_team = "<Player John Doe, Team: None>"
        self.assertEqual(repr(self.player), expected_no_team)


if __name__ == "__main__":
    unittest.main()
