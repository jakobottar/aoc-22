# pylint: disable=missing-function-docstring, redefined-outer-name
"""
advent of code 2022 day 3
jakob johnson
"""

FILENAME = "input.txt"


def print_bold(value):
    print("\033[1m" + value + "\033[0m")


def get_priority(char) -> int:
    priority = ord(char)
    if priority >= ord("a"):
        return priority - ord("a") + 1
    return priority - ord("A") + 27


def process_line(line) -> int:
    # split line in two
    first = set(line[: len(line) // 2])
    second = set(line[len(line) // 2 :])

    # get common character (always only 1)
    common = list(first & second)[0]

    # get priority num
    return get_priority(common)


def process_group(group):
    # convert to sets
    group = [set(elf) for elf in group]

    # get common character (always only 1)
    common = list(group[0] & group[1] & group[2])[0]

    # get priority num
    return get_priority(common)


with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

# part 1
total_priority = sum(list(map(process_line, lines)))

print_bold("part 1:")
print(f"total priority: {total_priority}")

# part 2
total_priority = sum(list(map(process_group, zip(*[iter(lines)] * 3))))

print_bold("part 2:")
print(f"total priority: {total_priority}")
