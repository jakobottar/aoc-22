# pylint: disable=missing-function-docstring, missing-class-docstring, redefined-outer-name
"""
advent of code 2022 day 5
jakob johnson
"""

from queue import LifoQueue

FILENAME = "input.txt"
INSTR_START = 10  # TODO: get this dynamically


class CargoShip:
    def __init__(self, num_cols, init_arr, crate_mover_version=9000) -> None:
        self.version = crate_mover_version

        self.stacks = []
        for i in range(num_cols):
            stack = LifoQueue(999)
            for box in init_arr[i]:
                stack.put(box)
            self.stacks.append(stack)

    def move(self, instruction):
        count, from_stack, to_stack = instruction

        crane = [self.stacks[from_stack - 1].get() for _ in range(count)]
        if self.version == 9001:
            crane.reverse()

        for box in crane:
            self.stacks[to_stack - 1].put(box)

    def print(self) -> None:
        for i, stack in enumerate(self.stacks):
            print(f"{i+1}: {stack.queue}")

    def get_top_boxes(self) -> str:
        top_boxes = ""

        copy_stacks = self.stacks.copy()

        for stack in copy_stacks:
            top_boxes += stack.get()[1]

        return top_boxes


def parse_instruction(instr):
    _, count, _, from_stack, _, to_stack = instr.split(" ")

    return (int(count), int(from_stack), int(to_stack))


def print_bold(value):
    print("\033[1m" + value + "\033[0m")


with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# get initial box locations
*boxes, cols = lines[: INSTR_START - 1]
boxes.reverse()

NUM_COLS = [int(c) for c in cols if c != " "][-1]

# parse them an put them in to an array
init_arr = [[] for _ in range(NUM_COLS)]
for line in boxes:
    for i in range(NUM_COLS):
        lower = i * 4
        upper = ((i + 1) * 4) - 1
        next_box = line[lower:upper]
        if next_box != "   ":
            init_arr[i].append(next_box)

# get the instructions
instructions = lines[INSTR_START:]
instructions = list(map(parse_instruction, instructions))

# part 1
print_bold("part 1:")

# generate the CargoShip class
ship = CargoShip(NUM_COLS, init_arr, 9000)

for instr in instructions:
    # print(instr)
    ship.move(instr)
    # ship.print()

print(f"top boxes: {ship.get_top_boxes()}")

# part 2
print_bold("part 2:")

# generate the CargoShip class
ship = CargoShip(NUM_COLS, init_arr, 9001)
for instr in instructions:
    # print(instr)
    ship.move(instr)
    # ship.print()

print(f"top boxes: {ship.get_top_boxes()}")
