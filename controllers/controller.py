from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/instructions')
def instructions():
    return render_template("instructions.html")

@app.route('/game')
def game():
    return render_template("game.html")

@app.route('/game/<gesture1>/<gesture2>')
def game_play_url(gesture1, gesture2):
    player1 = Player("Craig", gesture1)
    player2 = Player("Jayne", gesture2)
    player3 = Player("Jimmy", gesture1)
    player4 = Player("Marco", gesture2)
    game1 = Game(player1, player2)
    game2 = Game(player3, player4)
    play = play_game(game1)
    return render_template("game.html", play=play)

# created form on game.html and the app.route below but not finished
@app.route('/play')
def game_play():
    return render_template("play.html")

@app.route('/play', methods=["POST"])
def game_play2():
    gesture1 = request.form["gesture1"]
    gesture2 = request.form["gesture2"]
    name1 = request.form["name1"]
    name2 = request.form["name2"]
    player1 = Player(name1, gesture1)
    player2 = Player(name2, gesture2)
    game1 = Game(player1, player2)
    play2 = play_game(game1)
    return render_template("play.html", play2=play2)
    # return redirect('/play')