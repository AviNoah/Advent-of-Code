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

    def travel(self, row, col, from_dir: str) -> list:
        # Travel and return a list of pipes traveled to.

        if self.directions["north"] and from_dir != "north":
            self.travel(row - 1, col, "south")
        if self.directions["south"] and from_dir != "south":
            self.travel(row + 1, col, "north")
        if self.directions["east"] and from_dir != "east":
            self.travel(row, col - 1, "west")
        if self.directions["west"] and from_dir != "west":
            self.travel(row, col + 1, "east")


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


def find_loop() -> int:
    global pipe_grid
    # Return farthest point in a loop from starting point
    grid = [[[0] * len(pipe_grid[0])] * len(pipe_grid)]  # Init a grid of 0's
    s_row, s_col = find_S_coordinates(pipe_grid)

    # There are only two pipes actually coming from S, then, every other pipe in the main loop
    # is exclusively connected to two other pipes.


def part1():
    result = find_loop()


def part2():
    pass


def main():
    get_pipes()
    part1()
    part2()


if __name__ == "__main__":
    main()
