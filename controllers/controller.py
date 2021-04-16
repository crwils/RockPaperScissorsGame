from flask import render_template, request
from app import app
from models.player import *
from models.game import *



@app.route('/<gesture1>/<gesture2>')
def home(gesture1, gesture2):
    player1 = Player("Craig", gesture1)
    player2 = Player("Jayne", gesture2)
    answer = rps_game(player1, player2)
    return f"{answer}"
