"""
advent of code 2022 day 2
jakob johnson
"""

FILENAME = "input.txt"


def print_bold(x):
    print("\033[1m" + x + "\033[0m")


def get_rps_score(you, opponent) -> int:

    rps_key = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    if rps_key[you] == rps_key[opponent]:
        return 3  # score for draw
    if rps_key[you] == "rock":
        if rps_key[opponent] == "scissors":
            return 6  # score for win
        return 0  # loss, opponent == paper
    if rps_key[you] == "paper":
        if rps_key[opponent] == "rock":
            return 6  # score for win
        return 0  # loss, opponent == scissors
    else:  # you == scissors
        if rps_key[opponent] == "paper":
            return 6  # score for win
        return 0  # loss, opponent == rock


def get_shape_score(opponent, outcome) -> int:

    opponent_key = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }

    your_key = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    if outcome == "X":  # lose
        if opponent_key[opponent] == "rock":
            return your_key["scissors"]
        if opponent_key[opponent] == "paper":
            return your_key["rock"]
        return your_key["paper"]  # opponent == scissors
    if outcome == "Y":  # draw
        return your_key[opponent_key[opponent]]
    if outcome == "Z":  # win
        if opponent_key[opponent] == "rock":
            return your_key["paper"]
        if opponent_key[opponent] == "paper":
            return your_key["scissors"]
        return your_key["rock"]  # opponent == scissors


# read lines from file
with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()

# part 1
# set up scoring key
scoring_dict_1 = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

total_score = 0
for line in lines:
    line = line.strip().split(" ")
    total_score += scoring_dict_1[line[1]] + get_rps_score(line[1], line[0])

print_bold("part 1:")
print(f"total score: {total_score}")

# part 2
# set up scoring key
scoring_dict_2 = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

total_score = 0
for line in lines:
    line = line.strip().split(" ")
    total_score += scoring_dict_2[line[1]] + get_shape_score(line[0], line[1])

print_bold("part 2:")
print(f"total score: {total_score}")
