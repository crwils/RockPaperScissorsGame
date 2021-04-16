class Game:
    pass

    # def __init__(self, player1, player2):
    #     self.player1 = player1
    #     self.player2 = player2
valid_gestures = ["rock", "paper", "scissors"]

def rps_game(player1, player2):
    if (player1 not in valid_gestures) or (player2 not in valid_gestures):
        return f"Invalid entry!"
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
        return f"Player 1 wins by playing {player1}!"
    elif (player1 == "rock" and player2 == "paper") or (player1 == "paper" and player2 == "scissors") or (player1 == "scissors" and player2 == "rock"):
        return f"Player 2 wins by playing {player2}!"
    else:
        if player1 == player2:
            return None