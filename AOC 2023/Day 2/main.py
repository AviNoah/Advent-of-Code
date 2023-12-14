import re
from functools import reduce

id_pattern = r"game (\d+)"
color_pattern = r"(?: (\d+) (blue|red|green))+,*"
id_pattern = re.compile(id_pattern)
color_pattern = re.compile(color_pattern)


# Define monad to log game data
class game_bag:
    def __init__(self, game_id: int, bag: dict()):
        self.game_id = game_id
        self.required_bag_to_play: dict = (
            bag  # The minimum number of balls required to play
        )

    def get_id(self) -> int:
        return self.game_id

    def get_bag_power(self) -> int:
        # A bag power is equal to the numbers of red, green, and blue balls multiplied together
        values = self.required_bag_to_play.values()
        return reduce(lambda a, b: a * b, values)

    def is_smaller_than_other(self, other_bag: dict) -> bool:
        # Return whether curr_bag has more or less the same number of balls of each color as bag
        keys = other_bag.keys()
        values = [self.get(key, 0) for key in keys]
        return all([a <= b for a, b in zip(values, other_bag.values())])

    def get_bag(self) -> dict:
        return self.required_bag_to_play


def get_bags() -> list:
    # Get list of game_bags from file
    with open("input.txt", "r") as f:
        lines: list = f.readlines()

    def get_bag_from_line(line: str) -> game_bag:
        # Return the id if the bag in the game might be the given Bag, return None otherwise.
        line: str = line.lower()

        # Each game MUST have id
        game_id, data = line.split(":", maxsplit=1)
        game_id: int = int(re.match(id_pattern, game_id).group(1))  # Get id

        # Each game might not necessarily have data
        matches: list = re.findall(color_pattern, data)

        curr_bag: dict = dict()

        for match in matches:
            val, color = match  # Get value and color, discard string
            # Initialize to zero if not exists in bag yet, get max
            val = max(int(val), curr_bag.get(color, 0))
            curr_bag[color] = val

        return game_bag(game_id, curr_bag)

    return [get_bag_from_line(line) for line in lines]


def get_possible_bags(bag: dict) -> list:
    # Returns a list of ids of bags that contain at most the same amount of colored balls as in bag

    game_bags = get_bags()

    possible_game_bags: list = [
        game_bag for game_bag in game_bags if game_bag.is_smaller_than_other(bag)
    ]

    possible_game_bags: list = [
        game_bag for game_bag in possible_game_bags if game_bag is not None
    ]

    return possible_game_bags


if __name__ == "__main__":
    goal_bag: dict = {"red": 12, "green": 13, "blue": 14}  # RGB
    game_bags: list = get_possible_bags(goal_bag)  # get game bags

    # Get ids of game bags
    result_ids: list = [game_bag.get_id() for game_bag in game_bags]
    result_powers: list = [game_bag.get_bag_power() for game_bag in game_bags]
    print(sum(result_ids))
    print(sum(result_powers))
