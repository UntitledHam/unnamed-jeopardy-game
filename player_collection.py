from player import Player


class PlayerCollection:
    def __init__(self):
        self.players = []

    def add_player(self, name: str):
        """
        Adds a player to the players list.
        :param name: Name of the player to add.
        :post: players will have another player.
        """
        self.players.append(Player(name))

    def sort_players(self):
        """
        Sorts players by their score for the leader board.
        :post: Players are sorted by score (High to Low).
        """
        self.players.sort(key=lambda p: p.score, reverse=True)
