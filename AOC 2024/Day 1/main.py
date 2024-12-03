from dataclasses import dataclass
from typing import Any, Generator, Optional


with open("input.txt", "r") as f:
    lines: list = f.readlines()

    data = [line.strip().split("   ") for line in lines]
    data = [(int(row[0]), int(row[1])) for row in data]


@dataclass
class TreeNode:
    value: Any
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    def insert(self, value: Any):
        if self.value > value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def list_nodes(self) -> Generator[Any, None, None]:
        "Yield values in ascending order"
        if self.left:
            yield from self.left.list_nodes()
        yield self.value
        if self.right:
            yield from self.right.list_nodes()


def part1():
    "We basically have to sort both lists from smallest to largest and pair them"
    "A good data structure for this is a binary tree"
    global data
    first_row, *rest_of_data = data
    left_root, right_root = TreeNode(first_row[0]), TreeNode(first_row[1])

    for left, right in rest_of_data:
        left_root.insert(left)
        right_root.insert(right)

    distances = 0
    for left, right in zip(left_root.list_nodes(), right_root.list_nodes()):
        distances += abs(left - right)

    return distances


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
