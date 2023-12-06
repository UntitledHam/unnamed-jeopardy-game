from flask import Flask
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
}
.container div {
  background-color: blue;
  aspect-ratio: 1;
  text-align: center;
  color: white;
  font-family: "Times New Roman", Times, serif;
  font-size: 240%;
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
        {game.ask_question("music", 500)}
        
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run("localhost", debug=True)
