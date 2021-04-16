from flask import render_template, request
from app import app
from models.player import *
from models.game import *



@app.route('/<gesture1>/<gesture2>')
def home(gesture1, gesture2):
    player1 = Player("Craig", gesture1)
    player2 = Player("Jayne", gesture2)
    player3 = Player("Jimmy", gesture1)
    player4 = Player("Marco", gesture2)
    game1 = Game(player1, player2)
    game2 = Game(player3, player4)

    play = play_game(game1)
    return render_template("home.html", play=play)