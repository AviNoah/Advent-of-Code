from dataclasses import dataclass
from typing import Any


with open("input.txt", "r") as f:
    lines: list = f.readlines()

    data = [line.strip().split("   ") for line in lines]
    data = [(int(row[0]), int(row[1])) for row in data]


@dataclass
class TreeNode:
    value: Any
    left: "TreeNode" | None = None
    right: "TreeNode" | None = None

    def insert(self, value: Any):
        if self.value <= value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)


def part1():
    "We basically have to sort both lists from smallest to largest and pair them"
    "A good data structure for this is a binary tree"


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
