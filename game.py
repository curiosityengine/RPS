import random

choices = ["Rock", "Paper", "Scissors"]

def play_game(player):
    cpu = random.choice(choices)
    result_msg = ""
    player_score = 0
    cpu_score = 0

    if player not in choices:
        return {"error": "Invalid move. Choose Rock, Paper or Scissors."}

    if player == cpu:
        result_msg = "It's a tie!"
    elif player == "Rock":
        if cpu == "Paper":
            result_msg = f"You lost! {cpu} covers {player}"
            cpu_score += 1
        else:
            result_msg = f"You won! {player} crushes {cpu}"
            player_score += 1
    elif player == "Paper":
        if cpu == "Rock":
            result_msg = f"You won! {player} covers {cpu}"
            player_score += 1
        else:
            result_msg = f"You lost! {cpu} cuts {player}"
            cpu_score += 1
    elif player == "Scissors":
        if cpu == "Rock":
            result_msg = f"You lost! {cpu} crushes {player}"
            cpu_score += 1
        else:
            result_msg = f"You won! {player} cuts {cpu}"
            player_score += 1

    return {
        "player": player,
        "cpu": cpu,
        "result": result_msg
    }
