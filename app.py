from flask import Flask, request
from game import Game

app = Flask(__name__)
game = Game()

test_players = {"Jeff": 100, "Jimbo": 500, "Scott": 1000, "Abe": 5000, "Andrew": 3500}
for name, score in test_players.items():
    game.players.add_player(name)
    game.players.find_player_by_name(name).score = score
category_names = ["food_and_drink", "music", "geography", "random", "random"]
game.generate_categories(category_names)


with open("board-style.css", "r") as f:
    style = f.read()


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
        {game.generate_board_html()}
        
    </body>
    </html>
    """

    return html


@app.route("/ask-question")
def ask_question():
    category_name = request.args.get("category", "")
    point_value = int(request.args.get("point-value", ""))
    html = ""
    try:
        html += f"{game.ask_question(category_name, point_value)}"
    except ValueError:
        return "<h1>Invalid Question</h1>"

    return html
if __name__ == "__main__":
    app.run("localhost", debug=True)
