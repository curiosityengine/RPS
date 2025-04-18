from flask import Flask, render_template, request
from game import play_game

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    player_move = request.form["move"]
    result = play_game(player_move)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
