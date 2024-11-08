import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestPlayerReader(unittest.TestCase):
    def setUp(self):
        self.stats_service = StatisticsService(PlayerReaderStub())

    def join_player_names(self, players: list):
        return " ".join(list(map(lambda p: p.name, players)))

    def test_search_returns_player(self):
        self.assertEqual(
            self.stats_service.search("Kur").name,
            PlayerReaderStub().get_players()[2].name
            )

    def test_search_returns_none_when_name_not_found(self):
        self.assertIsNone(self.stats_service.search("Seppo Räty"))

    def test_team_is_filtered_right(self):
        team = self.stats_service.team("EDM")
        self.assertEqual(
            self.join_player_names(team),
            "Semenko Kurri Gretzky"
        )

    def test_returns_empty_list_when_team_not_found(self):
        team = self.stats_service.team("JYP")
        self.assertEqual(len(team), 0)

    def test_top_returns_right_players(self):
        top_2 = self.stats_service.top(2)
        self.assertEqual(
            self.join_player_names(top_2),
            "Gretzky Lemieux"
        )

        top_4 = self.stats_service.top(4)
        self.assertEqual(
            self.join_player_names(top_4),
            "Gretzky Lemieux Yzerman Kurri"
        )
