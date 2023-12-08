from player import Player
from flask import request


class PlayerCollection:
    def __init__(self):
        """
        Creates a PlayerCollection with a list of players
        """
        self.players = []
        self.alphabetical_players = []
        self.current_player_turn = None

    def add_player(self, name: str):
        """
        Adds a player to the players list.
        :param name: Name of the player to add.
        :raise ValueError: if player already exists or are more than 4 players
        :post: players will have another player.
        """
        player_names = list(map(lambda p: p.name, self.players))
        if name in player_names:
            raise ValueError("Player Already Exists.")
        player = Player(name)
        if len(self.players) >= 4:
            raise ValueError("Cannot have more than 4 players.")
        if len(name) == 0:
            raise ValueError("Player name must not be empty.")
        self.players.append(player)
        self.alphabetical_players.append(player)
        self.alphabetical_players.sort(key=lambda p: p.name)

    def remove_player(self, player_name: str):
        """
        Removes a player from the player list
        :param player_name: Name of the player to remove
        :post: players will have one less player
        """
        player = self.find_player_by_name(player_name)
        self.players.remove(player)
        self.alphabetical_players.remove(player)
        self.current_player_turn = None

    def reset_all_players(self):
        """
        Sets every player's score to 0
        :post: every player in players has 0 score
        """
        for player in self.players:
            player.score = 0
        self.current_player_turn = None

    def next_turn(self):
        """
        Cycles to next player in alphabetical_players
        :post: sets current_player_turn to next player
        """
        self.alphabetical_players.sort(key=lambda p: p.name)
        skip = False
        if self.current_player_turn is None:
            self.current_player_turn = self.alphabetical_players[0]
            skip = True
        player_index = self.alphabetical_players.index(self.current_player_turn)
        if player_index < len(self.alphabetical_players) - 1 and not skip:
            player_index += 1
        else:
            player_index = 0

        self.current_player_turn = self.alphabetical_players[player_index]

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

    def get_top_player(self) -> Player:
        """
        Returns the object of the top player.
        :post: Sorts the players.
        :return: The object of the top player.
        """
        self.sort_players()
        return self.players[0]

    def generate_player_list_html(self) -> str:
        """
        Generates html for player list to be used in app
        :return: html for player list
        """
        if len(self.players) == 0:
            return "No players added."
        output = ""
        for i in range(len(self.players)):
            output += f"""<p>{i+1}: {self.players[i].name}
            <a href="/remove-player?player-name={self.players[i].name}">
                remove
            </a>
            </p>
            """

        return output

    def generate_leaderboard_html(self) -> str:
        """
        Generates the HTML for displaying the leaderboard.
        :post: Sorts the players.
        :return: The HTML of the leaderboard.
        """
        category = request.args.get("category", "")
        player_name = request.args.get("player-name", "")
        point_value = int(request.args.get("point-value", "0"))
        skip_button = ""
        if category != "" and player_name == "":
            skip_button += f"<a href=/skip-question?category={category}&point-value={point_value}>Skip Question</a>"
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
        <h1>
            {self.current_player_turn.name}'s Turn
        </h1>
        <br>
        <h2>
            {skip_button}
        </h2>
        <br>
        </div>"""

