from flask import Flask
from flaskwebgui import FlaskUI

debug_mode = True

app = Flask(__name__)


@app.route("/")
def home():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Window Size Test</title>
    </head>
    <body>
        Hello World
    </body>
    </html>
    """

    return html


if __name__ == "main":
    app.run("localhost", debug=True)
