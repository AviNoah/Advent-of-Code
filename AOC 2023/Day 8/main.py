# First line is input to traverse graph
# Next lines are the definition of a node network, Node = (Left_child, Right_child)
# Start at Node AAA, according to the RL inputs, traverse either left or right in every node

# Performing this sequence for a certain number of periods P, will eventually land you on ZZZ
# So the total steps are P * len(input)

# Find total steps
import re

node_pattern: re.Pattern = re.compile(r"[A-Z]{3}")

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class bi_node:
    def __init__(self, label: str, left: str, right: str):
        self.label: str = label
        self.left = left  # The label of left
        self.right = right  # The label of right

    @staticmethod
    def from_line(line: str):
        # Return a bi_node object with relevant labels
        global node_pattern
        label, left, right = node_pattern.findall(line)
        return bi_node(label, left, right)

    def __str__(self):
        return f"{self.label} = ({self.left}, {self.right})"


def get_separator() -> int:
    # Returns the separator between node inputs and directions

    global lines
    for i, line in enumerate(lines):
        if line == "\n":
            # Finished parsing
            return i


def get_directions() -> list:
    global lines
    directions: list = lines[: get_separator()]
    directions: str = "".join(directions).replace("\n", "")  # Remove \n

    return list(directions)


def get_nodes() -> dict:
    global lines
    nodes: list = lines[get_separator() + 1 :]
    nodes: list = [bi_node.from_line(node) for node in nodes]

    return dict({node.label: node} for node in nodes)


def traverse(directions: list, nodes: dict) -> int:
    # Return the amount of steps needed to reach ZZZ from AAA
    steps = 0
    node_obj: bi_node = nodes.get("AAA")
    periods = 0

    while node_obj.label != "ZZZ":
        periods += 1
        for d in directions:
            steps += 1
            if d == "R":
                node_obj = node_obj.right
            elif d == "L":
                node_obj = node_obj.left
            else:
                raise Exception(f"Invalid input: {d}")

    return steps


def part1():
    directions: list = get_directions()
    print(directions)
    nodes: dict = get_nodes()
    for label, node in nodes:
        print(node)


def main():
    part1()


if __name__ == "__main__":
    main()
