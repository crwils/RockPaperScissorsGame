from flask import render_template, request
from app import app
from models.player import *
from models.game import *
# from models.player import Player


@app.route('/<player1>/<player2>')
def home(player1, player2):
    answer = rps_game(player1, player2)
    return f"{answer}"

    # player1 = Player("Craig", <player1>)
    # player2 = Player("Jayne", <player2>)