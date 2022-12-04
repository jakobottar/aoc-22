# pylint: disable=missing-function-docstring, redefined-outer-name
"""
advent of code 2022 day 4
jakob johnson
"""

FILENAME = "input.txt"


def print_bold(value):
    print("\033[1m" + value + "\033[0m")


def get_range(assignment):
    return set(range(int(assignment[0]), int(assignment[1]) + 1))


def is_fully_overlapping(line):
    # create sets
    pair = [a.split("-") for a in line.split(",")]
    pair = list(map(get_range, pair))

    # get intersection
    return pair[0] & pair[1] in (pair[0], pair[1])


def is_overlapping(line):
    # create sets
    pair = [a.split("-") for a in line.split(",")]
    pair = list(map(get_range, pair))

    # get intersection
    return len(pair[0] & pair[1]) != 0


with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

# part 1
print_bold("part 1:")
print(f"number overlapping: {sum(list(map(is_fully_overlapping, lines)))}")

# part 2
print_bold("part 2:")
print(f"number overlapping: {sum(list(map(is_overlapping, lines)))}")
