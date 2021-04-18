from controllers import *


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
valid_gestures = ["rock", "paper", "scissors"]

def play_game(game):
    if (game.player1.gesture not in valid_gestures) or (game.player2.gesture not in valid_gestures):
        return f"Invalid entry!"
    elif (game.player1.gesture == "rock" and game.player2.gesture == "scissors") or (game.player1.gesture == "paper" and game.player2.gesture == "rock") or (game.player1.gesture == "scissors" and game.player2.gesture == "paper"):
        return f"Result: {game.player1.name} wins by playing {game.player1.gesture}!"
    elif (game.player1.gesture == "rock" and game.player2.gesture == "paper") or (game.player1.gesture == "paper" and game.player2.gesture == "scissors") or (game.player1.gesture == "scissors" and game.player2.gesture == "rock"):
        return f"Result: {game.player2.name} wins by playing {game.player2.gesture}!"
    else:
        if game.player1.gesture == game.player2.gesture:
            #return None
            return "It's a draw! Go again. "
