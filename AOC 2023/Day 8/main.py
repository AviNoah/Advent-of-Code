# First line is input to traverse graph
# Next lines are the definition of a node network, Node = (Left_child, Right_child)
# Start at Node AAA, according to the RL inputs, traverse either left or right in every node

# Performing this sequence for a certain number of periods P, will eventually land you on ZZZ
# So the total steps are P * len(input)

# Find total steps
import re
from math import lcm

node_pattern: re.Pattern = re.compile(r"[A-Z]{3}")

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class bi_node:
    def __init__(self, label: str, left: str, right: str):
        self.label: str = label
        self.left = left  # The label of left
        self.right = right  # The label of right

    def get_next(self, inp: str) -> str:
        # Return the label of the given input
        if inp == "R":
            return self.right
        elif inp == "L":
            return self.left

        raise Exception(f"Invalid input: {inp}")

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


def get_directions() -> str:
    global lines
    directions: list = lines[: get_separator()]
    directions: str = "".join(directions).replace("\n", "")  # Remove \n

    return str(directions)


def get_nodes() -> dict:
    global lines
    nodes: list = lines[get_separator() + 1 :]
    nodes: list = [bi_node.from_line(node) for node in nodes]

    return dict({node.label: node for node in nodes})


def traverse(directions: str, nodes: dict) -> int:
    # Return the amount of steps needed to reach ZZZ from AAA
    steps = 0
    node_obj: bi_node = nodes.get("AAA")
    periods = 0

    while node_obj.label != "ZZZ":
        periods += 1
        for d in directions:
            steps += 1
            node_obj = nodes.get(node_obj.get_next(d))

    return steps


def traverse_multiple(directions: str, nodes: dict) -> int:
    node_objs: list[bi_node] = [nodes[key] for key in nodes.keys() if key[-1] == "A"]

    steps = 0
    dir_len = len(directions)

    periods = 1
    period_step = 0

    while node_objs:
        for d in directions:
            node_objs: list = [
                nodes.get(node_obj.get_next(d)) for node_obj in node_objs
            ]

        old_len = len(node_objs)

        # Remove node_objs that have already reached a Z state
        node_objs = list(filter(lambda node: node.label[-1] != "Z", node_objs))

        # Period frequency is the amount of times dir len must be stepped until we reach a
        # state where we have more nodes ending in Z - we can just ignore them in further steps using the periods

        # Add step's step times the period frequency we are in
        steps += dir_len * periods

        if len(node_objs) < old_len:
            # We reached a new period frequency, it is old period * LCM(period_step, old period)
            # Assume we have current freq and another bigger freq since it has not appeared yet,
            # their multiplication definitely returns all Z, but if they share common multiples they meet
            # much earlier (for example 2, 4 meet after 2 instead of 8, but 6, 7 meet at 42)
            print(f"Periods is now: {periods}")
            periods *= lcm(periods + period_step, periods)
            period_step = 0

        period_step += 1

    print(f"Periods is now: {periods}")
    return steps


def part1():
    directions: str = get_directions()
    nodes: dict = get_nodes()

    print(f"Total steps for part 1: {traverse(directions, nodes)}")


def part2():
    directions: str = get_directions()
    nodes: dict = get_nodes()

    print(f"Total steps for part 2: {traverse_multiple(directions, nodes)}")


def main():
    #  part1()  # Solution was 19241
    part2()  # Last solution was 576417


if __name__ == "__main__":
    main()
