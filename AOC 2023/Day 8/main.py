# First line is input to traverse graph
# Next lines are the definition of a node network, Node = (Left_child, Right_child)
# Start at Node AAA, according to the RL inputs, traverse either left or right in every node

# Performing this sequence for a certain number of periods P, will eventually land you on ZZZ
# So the total steps are P * len(input)

# Find total steps


with open("input.txt", "r") as f:
    lines: list = f.readlines()


class bi_node:
    def __init__(self, label: str, left, right):
        self.label: str = label
        self.left = left
        self.right = right


def part1():
    ...


def main():
    part1()


if __name__ == "__main__":
    main()
