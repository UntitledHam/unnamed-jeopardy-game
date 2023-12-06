import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_create_player(self):
        bob = Player("Bob")
        self.assertEquals("Bob", bob.name)

    def test_change_score(self):
        bob = Player("Bob")
        self.assertEquals(bob.score, 0)
        bob.change_score(300)
        self.assertEquals(bob.score, 300)
        bob.change_score(-100)
        self.assertEquals(bob.score, 200)
