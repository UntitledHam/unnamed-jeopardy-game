from flask import Flask, request, redirect
from game import Game
from api_request import generate_category_dropdowns

app = Flask(__name__)
game = Game()

category_names = ["random", "random", "random", "random", "random"]
game.generate_categories(category_names)

with open("styles/board-style.css", "r") as f:
    board_style = f.read()

with open("styles/question-style.css", "r") as f:
    question_style = f.read()

with open("styles/win_screen_style.css", "r") as f:
    win_screen_style = f.read()

with open("styles/homepage-style.css", "r") as f:
    homepage_style = f.read()


@app.route("/")
def home():
    game.reset()
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                {homepage_style}
            </style>
            <title>
                Untitled Jeopardy Game
            <title>
            <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
        </head>
        <body>
            <h1>
                Unnamed Jeopardy Game:
            </h1>
            <p>
            <h2>
                Players (Max of 4):
            </h2>
            <p>
                {game.players.generate_player_list_html()}
            </p>'
            <h2>
                Create Player
            </h2>
            <form action="/add-player" method="post">
                <label>
                    Player name: 
                    <input type="text" name="player_name">
                </label>
                <input type='submit' value="Create Player">
            </form>
            <h2>
                Choose Your Categories:
            </h2>
            <form action="/set-categories" method="post">
                {generate_category_dropdowns()}
                <br>
                <br>
                <input type='submit' value="Play">
            </form> 
        </body>
    </html>
    """
    return html


@app.route("/set-categories", methods=["POST"])
def set_categories():
    categories = []
    for i in range(5):
        categories.append(request.form.get(f"option-{i}", "random"))
    game.generate_categories(categories)
    return redirect("/board")


@app.route("/board")
def board():
    if len(game.players.players) == 0:
        return redirect("/")
    game.players.next_turn()
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Unnamed Jeopardy Game</title>
        <style>
            {board_style}
        </style>
    </head>
    <body>
        {game.players.generate_leaderboard_html()}
        {game.generate_board_html()}
        
    </body>
    </html>
    """

    if game.check_if_all_questions_are_answered():
        return redirect("/win-screen")

    return html


@app.route("/ask-question")
def ask_question():
    category_name = request.args.get("category", "")
    point_value = int(request.args.get("point-value", ""))
    try:
        question_html = game.ask_question(category_name, point_value)
    except ValueError:
        return "<h1>Invalid Question</h1>"

    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Unnamed Jeopardy Game</title>
            <style>
                {question_style}
            </style>
        </head>
        <body>
            {question_html}
        </body>
        </html>
        """
    return html


@app.route("/answer-question")
def answer_question():
    category_name = request.args.get("category", "")
    point_value = int(request.args.get("point-value", "0"))
    player_name = request.args.get("player", "")
    answer = int(request.args.get("answer", "0"))
    response_html = game.answer_question(category_name, point_value, player_name, answer)
    html = f"""
    <!DOCTYPE html>
        <html>
        <head>
            <title>Unnamed Jeopardy Game</title>
            <style>
                {win_screen_style}
            </style>
        </head>
        <body>
            {response_html}
        </body>
        </html>
    """

    return html


@app.route("/win-screen")
def win_screen():
    top_player = game.players.get_top_player()
    html = f"""
    <!DOCTYPE html>
        <html>
        <head>
            <title>Unnamed Jeopardy Game</title>
            <style>
                {win_screen_style}
            </style>
        </head>
        <body>
            <h1>
                Congratulations {top_player.name}, You Won!
            </h1>
            <p>
                You had a total of {top_player.score} points.
                <br><br>
                <a href="/">
                    Play Again
                </a>
            </p>
        </body>
        </html>
    """

    return html


@app.route("/add-player", methods=["POST"])
def add_player():
    try:
        player_name = str(request.form.get("player_name", ""))
    except ValueError:
        return redirect("/")

    try:
        game.players.add_player(player_name)
    except ValueError:
        return f"""
        <!DOCTYPE html>
        <html>
            <head>
            </head>
            <body>
                <p>
                    Cannot have more than 4 players.
                </p>
                <a href="/">
                    Return home.
                </a>
            </body>
        </html>
        """

    return redirect("/")


@app.route("/remove-player")
def remove_player():
    player_name = request.args.get("player-name", "")
    try:
        game.players.remove_player(player_name)
        return redirect("/")
    except ValueError:
        return "<h1>Invalid Player</h1>"


if __name__ == "__main__":
    app.run("localhost", debug=True)
