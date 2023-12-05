import unittest
from player_collection import PlayerCollection
from random import randint


class TestStringMethods(unittest.TestCase):
    def test_player_collection(self):
        players = PlayerCollection()
        player_names = ["Jimbo", "Jeff", "Abe", "Andrew", "Scott"]
        for name in player_names:
            players.add_player(name)
        for i in range(len(players.players)):
            self.assertEquals(players.players[i].name, player_names[i])

    def test_sort_players(self):
        players = PlayerCollection()
        player_names = ["Jimbo", "Jeff", "Abe", "Andrew", "Scott"]
        for name in player_names:
            players.add_player(name)

        for player in players.players:
            player.score += randint(100, 500)
        players.sort_players()

        for i in range(len(players.players)-1):
            self.assertGreaterEqual(players.players[i].score, players.players[i+1].score)




