# Find the shape of a pipe, marked S that will create a closed loop with other pipes surrounding it.
# Afterwards, walk along the loop and find the farthest pipe from it.

# Strategy - measure how far every pipe is from S, if two paths join at the SAME distance value, they
# MUST close a loop. this way we find the farthest point AND the main loop.

with open("input.txt", "r") as f:
    lines: list = f.readlines()

pipe_types: dict = {
    "|": "north-south",
    "-": "east-west",
    "L": "north-east",
    "J": "north-west",
    "7": "south-west",
    "F": "south-east",
    ".": "ground",  # No pipe
    "S": "east-west-north-south",  # Unknown pipe
}

cardinal_directions = ["south", "north", "east", "west"]
pipe_grid = None


class pipe:
    def __init__(self, symbol: str):
        global cardinal_directions
        self.symbol: str = symbol
        self.type: str = pipe_types.get(symbol, "ground")

        # Set which directions the pipe CAN lead to

        # A list of valid cardinals
        cardinals: list = self.type.split("-")
        if len(cardinals) == 1:
            cardinals: list = list()

        self.directions = dict.fromkeys(cardinal_directions, False)
        for key in cardinals:
            self.directions[key] = True

    def get_travel_path(self, row, col, from_dir) -> tuple:
        # Return a list of row, col, from_dir of paths we can take from current state.
        travel_path: tuple = None

        if self.directions["north"] and from_dir != "north":
            travel_path = (row - 1, col, "south")
        if self.directions["south"] and from_dir != "south":
            travel_path = (row + 1, col, "north")
        if self.directions["west"] and from_dir != "west":
            travel_path = (row, col - 1, "east")
        if self.directions["east"] and from_dir != "east":
            travel_path = (row, col + 1, "west")

        # Check if destination has a direction matching from_dir
        if not travel_path:
            return None  # No matching paths

        row, col, dir = travel_path
        if pipe_at(row, col).directions[dir]:
            return travel_path  # If other pipe has a receiving end
        return None

    def travel(self, row, col, from_dir: str) -> int:
        # The amount of steps needed to reach S
        steps = 0
        tmp = self

        while tmp.symbol != "S":
            steps += 1
            travel_path = tmp.get_travel_path(row, col, from_dir)
            if not travel_path:
                # Unable to travel further, return None
                return None

            row, col, from_dir = travel_path
            tmp = pipe_at(row, col)

        return steps


def pipe_at(row, col) -> pipe | None:
    global pipe_grid
    try:
        return pipe_grid[row][col]
    except IndexError:
        return None


def get_pipes():
    global lines, pipe_grid

    def pipes_from_line(line: str) -> list[pipe]:
        line: str = line.replace("\n", "")
        return [pipe(char) for char in line]

    pipe_grid = [pipes_from_line(line) for line in lines]


def find_S_coordinates() -> tuple[int, int]:
    global pipe_grid
    for row, pipe_row in enumerate(pipe_grid):
        for col, p in enumerate(pipe_row):
            if p.symbol == "S":
                return row, col

    return None


def count_steps() -> int:
    # Return farthest point in a loop from starting point
    s_row, s_col = find_S_coordinates()

    # Check from every direction of S
    travel_paths = list(
        [
            (s_row - 1, s_col, "south"),
            (s_row + 1, s_col, "north"),
            (s_row, s_col - 1, "west"),
            (s_row, s_col + 1, "east"),
        ]
    )

    for row, col, from_dir in travel_paths:
        p = pipe_at(row, col)
        if not p.directions[from_dir]:
            continue  # Invalid receiving end

        steps = p.travel(row, col, from_dir=from_dir)
        if steps:
            return steps + 1  # Count S as well

    return None


def part1():
    steps = count_steps()
    # Steps is always even, since there must be an equal amount of steps left and right,
    # and an equal amount of steps up and down, therefore the farthest point is always steps / 2 away
    if steps:
        print(f"The farthest point from the start is {steps //2 } steps away")
    else:
        print(f"No loop for S found!")


def part2():
    # Maybe the farthest point from S creates two corners of a rectangle allowing us to focus on one area
    # of the entire grid?
    pass


def main():
    get_pipes()
    part1()  # Solution was 6864
    part2()


if __name__ == "__main__":
    main()
