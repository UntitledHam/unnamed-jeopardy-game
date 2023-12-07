from player import Player


class PlayerCollection:
    def __init__(self):
        self.players = []
        self.alphabetical_players = []

    def add_player(self, name: str):
        """
        Adds a player to the players list.
        :param name: Name of the player to add.
        :post: players will have another player.
        """
        player = Player(name)
        self.players.append(player)
        self.alphabetical_players.append(player)
        self.alphabetical_players.sort(key=lambda p: p.name)

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

    def get_top_player(self):
        """
        Returns the object of the top player.
        :post: Sorts the players.
        :return: The object of the top player.
        """
        self.sort_players()
        return self.players[0]

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

        return f"""
        <div class="leaderboard">
        <h1>
            Leaderboard:
        </h1>
        <p>
            {leaderboard_html}
        </p>
        </div>"""

