from flask import Flask
from game import Game

app = Flask(__name__)
game = Game()

style = """ 
td {
  width: 33%; 
  padding-bottom: 33%; height: 0;
}
td div { 
position: absolute;
}
"""

test_players = {"Jeff": 100, "Jimbo": 500, "Scott": 1000, "Abe": 5000, "Andrew": 3500}
for name, score in test_players.items():
    game.players.add_player(name)
    game.players.find_player_by_name(name).score = score
category_names = ["random", "random", "random", "random", "random"]
game.generate_categories(category_names)




@app.route("/")
def home():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Unnamed Jeopardy Game</title>
        <style>
            {style}
        </style>
    </head>
    <body>
        {game.players.generate_leaderboard_html()}
        <br>
        {game.generate_board_html()}
        
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run("localhost", debug=True)
