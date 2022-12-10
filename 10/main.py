# pylint: disable=missing-function-docstring, missing-class-docstring, redefined-outer-name
"""
advent of code 2022 day 10
jakob johnson
"""

FILENAME = "input.txt"


def bold(value):
    return "\033[1m" + str(value) + "\033[0m"


with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()
lines = [line.strip().split(" ") for line in lines]

print(bold("part 1:"))
BKPOINTS = [20, 60, 100, 140, 180, 220]
lines_itr = iter(lines)
X = 1
signal_strength = 0
queued_op = None

for cycle in range(1, 241):

    # handle signal strength breakpoints
    if cycle in BKPOINTS:
        signal_strength += cycle * X

    # handle register and operations
    if queued_op:
        X += queued_op
        queued_op = None
    else:
        line = next(lines_itr)

        # noop cycle
        if line[0] == "noop":
            continue

        # addx cycle
        queued_op = int(line[1])

print(f"signal strength: {bold(signal_strength)}")

print(bold("part 2:"))
BKPOINTS = [40, 80, 120, 160, 200, 240]
lines_itr = iter(lines)
X = 1
queued_op = None

for cycle in range(1, 241):
    # handle crt
    crt_col = (cycle - 1) % 40
    if abs(crt_col - X) <= 1:
        print(bold("#"), end="")
    else:
        print(".", end="")

    # handle newline breakpoints
    if cycle in BKPOINTS:
        print("")

    # handle register and operations
    if queued_op:
        X += queued_op
        queued_op = None
    else:
        line = next(lines_itr)

        # noop cycle
        if line[0] == "noop":
            continue

        # addx cycle
        queued_op = int(line[1])
