from flask import render_template, request
from app import app
from models.player import *
from models.game import *
import random

@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/play')
def instructions():
    return render_template("play.html")

@app.route('/vs_friend/')
def game():
    return render_template("vs_friend.html")

@app.route('/vs_friend/<gesture1>/<gesture2>')
def game_play_url(gesture1, gesture2):
    player1 = Player("Craig", gesture1)
    player2 = Player("Jayne", gesture2)
    player3 = Player("Jimmy", gesture1)
    player4 = Player("Marco", gesture2)
    game1 = Game(player1, player2)
    game2 = Game(player3, player4)
    play = play_game(game1)
    return render_template("vs_friend.html", play=play)

@app.route('/vs_computer', methods=["GET", "POST"])
def game_play2():
    if request.method == 'GET':
        return render_template("vs_computer.html")
    if request.method == 'POST':
        gesture1 = request.form["gesture1"]
        # gesture2 = request.form["gesture2"]
        name1 = request.form["name1"]
        # name2 = request.form["name2"]
        player1 = Player(name1, gesture1)
        computer = Player("Computer", random.choice(valid_gestures))
        game1 = Game(player1, computer)
        play2 = play_game(game1)
        return render_template("result.html", play2=play2)