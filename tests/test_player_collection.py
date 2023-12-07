import unittest
from player_collection import PlayerCollection
from random import randint


class TestPlayerCollection(unittest.TestCase):
    #doesn't test for returns of html strings, as seeing the flask app does
    def test_player_collection_add_player_remove_player(self):
        players = PlayerCollection()
        player_names = ["Jimbo", "Jeff", "Abe", "Andrew"]
        for name in player_names:
            players.add_player(name)
        for i in range(len(players.players)):
            self.assertEquals(players.players[i].name, player_names[i])
        players.remove_player("Jeff")
        players.remove_player("Andrew")
        player_names_two = ["Jimbo", "Abe"]
        for i in range(len(players.players)):
            self.assertEquals(players.players[i].name, player_names_two[i])

    def test_find_player_by_name(self):
        players = PlayerCollection()
        player_names = ["Jimbo", "Jeff", "Abe", "Andrew"]
        for name in player_names:
            players.add_player(name)
        for i in range(len(players.players)):
            self.assertEquals(players.players[i], players.find_player_by_name(player_names[i]))

    def test_sort_players(self):
        players = PlayerCollection()
        player_names = ["Jimbo", "Jeff", "Abe", "Andrew"]
        for name in player_names:
            players.add_player(name)

        for player in players.players:
            player.score += randint(100, 500)
        players.sort_players()

        for i in range(len(players.players)-1):
            self.assertGreaterEqual(players.players[i].score, players.players[i+1].score)






