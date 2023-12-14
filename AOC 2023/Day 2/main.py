import re

id_pattern = r"game (\d+)"
color_pattern = r"(?: (\d+) (blue|red|green))+,*"
id_pattern = re.compile(id_pattern)
color_pattern = re.compile(color_pattern)


def main(bag: dict) -> list:
    # Returns a list of ids of bags that contain at most the same amount of colored balls as in bag

    with open("input.txt", "r") as f:
        lines: list = f.readlines()

    def is_smaller_than_bag(curr_bag: dict) -> bool:
        # Return whether curr_bag has more or less the same number of balls of each color as bag
        keys = bag.keys()
        values = [curr_bag.get(key, 0) for key in keys]
        return all([a <= b for a, b in zip(values, bag.values())])

    def might_be_bag(line: str) -> int:
        # Return the id if the bag in the game might be the given Bag, return None otherwise.
        line: str = line.lower()

        # Each game MUST have id
        id, data = line.split(":", maxsplit=1)
        id = re.match(id_pattern, id).group(1)  # Get id

        # Each game might not necessarily have data
        matches: list = re.findall(color_pattern, data)

        curr_bag: dict = dict()

        for match in matches:
            val, color = match  # Get value and color, discard string
            # Initialize to zero if not exists in bag yet, get max
            val = max(int(val), curr_bag.get(color, 0))
            curr_bag[color] = val

        if is_smaller_than_bag(curr_bag):
            return int(id)
        return None

    result_ids: list = [might_be_bag(line) for line in lines]
    result_ids: list = [id for id in result_ids if id is not None]
    return result_ids


if __name__ == "__main__":
    goal_bag: dict = {"red": 12, "green": 13, "blue": 14}  # RGB
    ids: list = main(goal_bag)
    print(sum(ids))
