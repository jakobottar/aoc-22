"""
advent of code 2022 day 1
jakob johnson
"""


def print_bold(x):
    print("\033[1m" + x + "\033[0m")


def count_calories(filename: str) -> None:
    elves = [0]

    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line == "\n":  # next elf
                elves.append(0)
            else:
                elves[-1] += int(line)

    # part 1: max calories
    print(f"num elves: {len(elves)}")
    print(f"max calories: {max(elves)}")

    # part 2: calories in top 3 elves
    elves.sort()
    print(f"sum of top 3 elves: {sum(elves[-3:])}")


if __name__ == "__main__":
    print_bold("example:")
    count_calories("example.txt")

    print_bold("\ninput:")
    count_calories("input.txt")
