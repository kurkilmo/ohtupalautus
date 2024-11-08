from player_reader import PlayerReader



class StatisticsService:
    def __init__(self, player_reader: PlayerReader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        # Alkuperäinen palautti yhden pelaajan liikaa
        return sorted_players[:how_many]
