import re
from functools import reduce

pattern = r"game (\d+):(?:( \d+ (?:blue|red|green))+,* )+;*"
pattern = re.compile(pattern)


def main(bag: dict) -> list:
    with open("input.txt", "r") as f:
        lines: list = f.readlines()

    def might_be_bag(line: str) -> int:
        # Return the id if the bag in the game might be the given Bag, return None otherwise.
        line: str = line.lower()
        match = re.match(pattern, line)

        if not match:
            return None

        id = match.group(0)
        return id

    result_ids: list = [might_be_bag(line) for line in lines]
    result_ids: list = [id for id in result_ids if id is not None]
    return result_ids


if __name__ == "__main__":
    goal_bag: dict = {"red": 12, "green": 13, "blue": 14}  # RGB
    main(goal_bag)
