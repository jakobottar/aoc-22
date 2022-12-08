# pylint: disable=missing-function-docstring, missing-class-docstring, redefined-outer-name
"""
advent of code 2022 day 8
jakob johnson
"""
import numpy as np

FILENAME = "input.txt"


def bold(value):
    return "\033[1m" + str(value) + "\033[0m"


def is_visible(forest, coords):
    row, col = coords
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


def get_scenic_score(forest, coords):
    row, col = coords
    height = forest[row, col]

    # TODO: there has to be a better way to do this...
    score = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        count = 0
        r, c = row + dx, col + dy
        while 0 <= r < forest.shape[0] and 0 <= c < forest.shape[1]:
            count += 1
            if forest[r, c] < height:
                r += dx
                c += dy
            else:
                break
        score *= count

    return score


with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()

forest = []
for line in lines:
    forest.append([int(tree) for tree in list(line.strip())])

forest = np.array(forest)

print(bold("part 1:"))

num_visible = sum(is_visible(forest, coords) for coords, _ in np.ndenumerate(forest))
print(f"found {bold(num_visible)} visible trees")

print(bold("part 2:"))

max_score = max(
    get_scenic_score(forest, coords) for coords, _ in np.ndenumerate(forest)
)
print(f"max scenic score: {bold(max_score)}")
