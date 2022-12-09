# pylint: disable=missing-function-docstring, missing-class-docstring, redefined-outer-name
"""
advent of code 2022 day 9
jakob johnson
"""
import numpy as np

FILENAME = "input.txt"


class RopeBridge:
    def __init__(self, num_knots=2) -> None:
        self.tail_location = set()
        self.knots = [(0, 0) for _ in range(num_knots)]

    def move(self, instruction):
        move_key = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
        direction, distance = instruction
        dx, dy = np.array(move_key[direction])
        for _ in range(distance):
            self.knots[0] = (self.knots[0][0] + dx, self.knots[0][1] + dy)

            for i in range(1, len(self.knots)):
                self.update_next_knot(i - 1, i)

            self.tail_location.add(self.knots[-1])

    def update_next_knot(self, first_idx, second_idx):
        hx, hy = self.knots[first_idx]
        tx, ty = self.knots[second_idx]
        dx, dy = hx - tx, hy - ty
        if abs(dx) <= 1 and abs(dy) <= 1:
            return

        mx = 1 if dx > 0 else 0 if dx == 0 else -1
        my = 1 if dy > 0 else 0 if dy == 0 else -1

        self.knots[second_idx] = (tx + mx, ty + my)


def bold(value):
    return "\033[1m" + str(value) + "\033[0m"


with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()
lines = [
    (direction, int(distance))
    for direction, distance in [line.strip().split(" ") for line in lines]
]

print(bold("part 1:"))
rb2 = RopeBridge(2)
for instr in lines:
    rb2.move(instr)

print(f"tail visited {len(rb2.tail_location)} locations")

print(bold("part 2:"))
rb10 = RopeBridge(10)
for instr in lines:
    rb10.move(instr)

print(f"tail visited {len(rb10.tail_location)} locations")
