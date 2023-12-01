from flask import Flask
from flaskwebgui import FlaskUI

debug_mode = True

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


if __name__ == "main":
    app.run("localhost", debug=True)
