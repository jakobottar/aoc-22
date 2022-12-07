# pylint: disable=missing-function-docstring, missing-class-docstring, redefined-outer-name
"""
advent of code 2022 day 7
jakob johnson
"""

FILENAME = "input.txt"
FILESYSTEM_SIZE = 70000000
UPDATE_SIZE = 30000000


def bold(value):
    return "\033[1m" + str(value) + "\033[0m"


class Node:
    def __init__(self, parent, name, size=0):
        self.parent = parent
        self.name = name
        self.size = size
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

        # if we can't find the child,
        raise ValueError(f"cannot find child {name}")

    def update_size(self) -> int:
        for child in self.children:
            self.size += child.update_size()

        return self.size

    def print(self, spacer=""):
        print(spacer, f"{self.name} - {self.size}")
        for child in self.children:
            child.print(spacer + "  ")


def count_num_below(node):
    count, total_size = 0, 0
    for child in node.children:
        c_count, c_total = count_num_below(child)
        count += c_count
        total_size += c_total

    if node.size < 100000:
        count += 1
        total_size += node.size

    return count, total_size


def size_of_dir_to_rm(node):
    if node.size < (UPDATE_SIZE - FREE_SPACE):
        return FILESYSTEM_SIZE + 1

    smallest_dir = node.size
    for child in node.children:
        c_smallest = size_of_dir_to_rm(child)
        smallest_dir = min(c_smallest, smallest_dir)

    return smallest_dir


with open(FILENAME, encoding="utf-8") as f:
    lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]

# make root dir
root = Node(None, "/", 0)
curr_node = root

for line in lines[1:]:
    line = line.split(" ")

    if line[0] == "$":  # handle instruction
        match line[1]:
            case "ls":  # do nothing, handled elsewhere
                continue
            case "cd":  # move to given node
                if line[2] == "..":
                    curr_node = curr_node.parent
                else:
                    curr_node = curr_node.find_child(line[2])

    else:  # handle adding file or dir
        if line[0] == "dir":
            new_node = Node(curr_node, line[1], 0)
            curr_node.add_child(new_node)
        else:
            curr_node.size += int(line[0])

# update folder sizes with children's info
root.update_size()

# traverse tree and count
print(bold("part 1:"))
num, size = count_num_below(root)
print(f"dirs found below 100000: {bold(num)}, and total size: {bold(size)}")

print(bold("part 2:"))
FREE_SPACE = FILESYSTEM_SIZE - root.size
print(f"smallest dir to delete: {bold(size_of_dir_to_rm(root))}")
