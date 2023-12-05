from flask import Flask
from game import Game

app = Flask(__name__)
game = Game()

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


if __name__ == "__main__":
    app.run("localhost", debug=True)
