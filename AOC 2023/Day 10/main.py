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

    def get_displacements(self, from_dir: str) -> list[tuple]:
        # Return possible displacements coming from from_dir
        vertical = list()
        horizontal = list()

        if "north" in self.cardinals and from_dir != "north":
            vertical.append(-1)
        if "south" in self.cardinals and from_dir != "south":
            vertical.append(1)
        if "east" in self.cardinals and from_dir != "east":
            horizontal.append(-1)
        if "west" in self.cardinals and from_dir != "west":
            horizontal.append(-1)

        results = [(0, v) for v in vertical]
        results.extend([(h, 0) for h in horizontal])
        return results


def get_pipe(pipe_grid, i, j) -> pipe | None:
    try:
        return pipe_grid[i][j]
    except IndexError:
        return None


def get_pipes() -> list[list[pipe]]:
    global lines

    def pipes_from_line(line: str) -> list[pipe]:
        line: str = line.replace("\n", "")
        return [pipe(char) for char in line]

    table = [pipes_from_line(line) for line in lines]
    return table


def find_S(pipes: list[list[pipe]]) -> tuple[int, int]:
    for row, pipe_row in enumerate(pipes):
        for col, p in enumerate(pipe_row):
            if p.symbol == "S":
                return row, col

    return None


def find_loop(pipe_grid: list[list[pipe]]) -> int:
    # Return farthest point in a loop from starting point
    grid = [[[0] * len(pipe_grid[0])] * len(pipe_grid)]  # Init a grid of 0's
    row, col = find_S(pipe_grid)

    # There are only two pipes actually coming from S, then, every other pipe in the main loop
    # is exclusively connected to two other pipes.

    def helper(r, c):
        ...

    dirs = get_pipe(pipe_grid, row, col).get_displacements()


def part1():
    pipes: list[list[pipe]] = get_pipes()
    result = find_loop(pipes)


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
