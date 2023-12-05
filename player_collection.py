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

    def find_player_by_name(self, name: str) -> Player:
        """
        Searches for the player of the matching name.
        :param name: The name to search for.
        :return: Player object that matches the given name.
        """
        for player in self.players:
            if player.name == name:
                return player
        raise ValueError("Player not found.")

    def sort_players(self):
        """
        Sorts players by their score for the leader board.
        :post: Players are sorted by score (High to Low).
        """
        self.players.sort(key=lambda p: p.score, reverse=True)

    def generate_leaderboard_html(self) -> str:
        """
        Generates the HTML for displaying the leaderboard.
        :post: Sorts the players.
        :return: The HTML of the leaderboard.
        """
        self.sort_players()
        leaderboard_html = ""
        for i in range(len(self.players)):
            leaderboard_html += f"{i+1}: {self.players[i].name}: {self.players[i].score}<br>"

        return f"""<h1>Leaderboard:</h1>{leaderboard_html}<br>"""

