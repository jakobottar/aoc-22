# pylint: disable=missing-function-docstring, missing-class-docstring, redefined-outer-name
"""
advent of code 2022 day 6
jakob johnson
"""

FILENAME = "input.txt"


def print_bold(value):
    print("\033[1m" + value + "\033[0m")


def unique(item) -> bool:
    return len(set(item)) == len(item)


def find_marker(encoded_string: str, marker_len: int) -> int:
    for i in range(marker_len, len(line)):
        marker = encoded_string[i - marker_len : i]
        if unique(marker):
            return i, marker


with open(FILENAME, encoding="utf-8") as f:
    line = f.readline().strip()

print_bold("part 1:")
count, marker = find_marker(line, 4)
print(f"found start-of-packet marker {marker} after {count} characters")

print_bold("part 2:")
count, marker = find_marker(line, 14)
print(f"found start-of-message marker {marker} after {count} characters")
