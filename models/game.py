from controllers import *


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

def rps_game(player1, player2):
    valid_gestures = ["rock", "paper", "scissors"]
    if (player1.gesture not in valid_gestures) or (player2.gesture not in valid_gestures):
        return f"Invalid entry!"
    elif (player1.gesture == "rock" and player2.gesture == "scissors") or (player1.gesture == "paper" and player2.gesture == "rock") or (player1.gesture == "scissors" and player2.gesture == "paper"):
        return f"Player 1 wins by playing {player1.gesture}!"
    elif (player1.gesture == "rock" and player2.gesture == "paper") or (player1.gesture == "paper" and player2.gesture == "scissors") or (player1.gesture == "scissors" and player2.gesture == "rock"):
        return f"Player 2 wins by playing {player2.gesture}!"
    else:
        if player1.gesture == player2.gesture:
            return None
