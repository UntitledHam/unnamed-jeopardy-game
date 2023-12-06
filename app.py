from flask import Flask, request
from game import Game

app = Flask(__name__)
game = Game()

test_players = {"Jeff": 100, "Jimbo": 500, "Scott": 1000, "Abe": 5000, "Andrew": 3500}
for name, score in test_players.items():
    game.players.add_player(name)
    game.players.find_player_by_name(name).score = score
category_names = ["music", "random", "random", "random", "random"]
game.generate_categories(category_names)


style = """ 

body {
    background-color: #301e83;
}

div {
    width: 70%;
    height: 70%;
    padding: 20px;
    margin: auto;
}
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  grid-gap: 5px;
  background-color: #000387;
}
.container div {
  background-color: blue;
  aspect-ratio: 1;
  text-align: center;
  color: white;
  font-family: "Times New Roman", Times, serif;
  font-size: 240%;
  border: 1px white solid;
}
"""



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
        <br>
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
