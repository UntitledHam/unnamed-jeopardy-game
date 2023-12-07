from flask import Flask, request, redirect
from game import Game

app = Flask(__name__)
game = Game()

test_players = {"Jeff": 100, "Scott": 1000, "Abe": 5000}
for name, score in test_players.items():
    game.players.add_player(name)
    game.players.find_player_by_name(name).score = score
category_names = ["food_and_drink", "music", "geography", "random", "random"]
game.generate_categories(category_names)
done_question = game.categories[0].get_question_by_point_val(300)
game.categories[0].done_questions.append(done_question)


with open("styles/board-style.css", "r") as f:
    board_style = f.read()

with open("styles/question-style.css", "r") as f:
    question_style = f.read()

with open("styles/win_screen_style.css", "r") as f:
    win_screen_style = f.read()


@app.route("/")
def home():
    game.reset()
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <style>
            </style>
        </head>
        <body>
            <h1>
                Unnamed Jeopardy Game:
            </h1>
            <h2>
                Players (Max of 4):
            </h2>
            <p>
                {game.players.generate_player_list_html()}
            </p>
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
        </body>
    </html>
    """
    return html


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
