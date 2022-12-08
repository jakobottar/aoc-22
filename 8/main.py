# pylint: disable=missing-function-docstring, missing-class-docstring, redefined-outer-name
"""
advent of code 2022 day 8
jakob johnson
"""
import numpy as np

FILENAME = "input.txt"


def bold(value):
    return "\033[1m" + str(value) + "\033[0m"


def is_visible(forest, row, col):
    if row == 0 or col == 0:
        return True
    if row == len(forest) - 1 or col == len(forest[row]) - 1:
        return True

    above = np.max(forest[:row, col])
    below = np.max(forest[row + 1 :, col])
    left = np.max(forest[row, :col])
    right = np.max(forest[row, col + 1 :])

    height = forest[row, col]
    return above < height or below < height or left < height or right < height


def get_scenic_score(forest, row, col):
    height = forest[row, col]

    # TODO: there has to be a better way to do this...
    above = 0
    for r in range(row - 1, -1, -1):
        above += 1
        if forest[r, col] >= height:
            break

    below = 0
    for r in range(row + 1, len(forest[row])):
        below += 1
        if forest[r, col] >= height:
            break

    left = 0
    for c in range(col - 1, -1, -1):
        left += 1
        if forest[row, c] >= height:
            break

    right = 0
    for c in range(col + 1, len(forest)):
        right += 1
        if forest[row, c] >= height:
            break

    return above * below * left * right


with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()

forest = []
for line in lines:
    forest.append([int(tree) for tree in list(line.strip())])

forest = np.array(forest)

print(bold("part 1:"))

count = 0
for row, forest_row in enumerate(forest):
    for col, _ in enumerate(forest_row):
        count += int(is_visible(forest, row, col))

print(f"found {bold(count)} visible trees")

print(bold("part 2:"))

max_score = -1
for row, forest_row in enumerate(forest):
    for col, _ in enumerate(forest_row):
        max_score = max(get_scenic_score(forest, row, col), max_score)


print(f"max scenic score: {bold(max_score)}")
