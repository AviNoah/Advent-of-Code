import re
from functools import reduce

pattern = r"game (?:(?:(\d+): (\d+ (?:blue|red|green)),)+;)+"
pattern = re.compile(pattern)


def main(bag: dict):
    with open("input.txt", "r") as f:
        lines: list = f.readlines()

    def max_dict(bag1: dict, bag2: dict) -> dict:
        # Return the maximum values from each bag for every key, both have same keys
        if bag1.keys() != bag2.keys():
            raise Exception("Incompatible bags")

        keys: list = list(bag1.keys())
        max_values = [max(bag1[key], bag2[key]) for key in keys]
        result = dict(zip(keys, max_values))

        return result

    def get_sets(line: str) -> list[dict]:
        # Given sets of subsets of picked dice, pick maximum amount of dice as dict.
        line: str = line.lower()
        matches: list = pattern.fullmatch(line)
        sets: list = ...

        return sets

    for line in lines:
        sets: list[dict] = get_sets(line)
        result = reduce(lambda a, b: max_dict(a, b), sets)

    # initialize to zero if any colors were not picked at all
    result: dict = max_dict({"red": 0, "green": 0, "blue": 0}, result)

    return result


if __name__ == "__main__":
    goal_bag: dict = {"red": 12, "green": 13, "blue": 14}  # RGB
    main(goal_bag)
