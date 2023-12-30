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

pipe_types_reversed: dict = {
    "|": "-",
    "-": "|",
    "L": "7",
    "J": "F",
    "7": "L",
    "F": "J",
    ".": ".",  # No pipe
    "S": "S",  #  Keep as S  # TODO: Maybe figure out what S needs to be
}

cardinal_directions = ["south", "north", "east", "west"]
pipe_grid = None


class pipe:
    def __init__(self, symbol: str):
        global cardinal_directions
        self.symbol: str = symbol
        self.type: str = pipe_types.get(symbol, "ground")
        self.is_in_closed_loop: bool = False
        self.is_squeeze_through: bool = False

        # Set which directions the pipe CAN lead to

        # A list of valid cardinals
        cardinals: list = self.type.split("-")
        if len(cardinals) == 1:
            cardinals: list = list()  # Empty list

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

    def travel_and_mark(self, row, col, from_dir: str):
        # Mark the main loop in a grid
        tmp = self

        while tmp.symbol != "S":
            travel_path = tmp.get_travel_path(row, col, from_dir)
            if not travel_path:
                # Unable to travel further, return None
                return None

            row, col, from_dir = travel_path

            pipe_grid[row][col].is_in_closed_loop = True
            tmp = pipe_at(row, col)

    def reverse(self):
        # Reverse type of pipe, return new
        global pipe_types_reversed
        symbol: str = pipe_types_reversed.get(self.symbol)
        return pipe(symbol)

    def does_connect(self, other) -> bool:
        # Return whether self and other can connected to each other (position is irrelevant)
        if not isinstance(other, pipe):
            return False

        valid_self_dirs = [key for key, value in self.directions.items() if value]
        # The reversed pipe of other shows what directions it accepts inputs from.
        valid_other_dirs = [key for key, value in other.directions.items() if not value]
        return any([o in valid_self_dirs for o in valid_other_dirs])


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


def figure_s_shape():
    global pipe_grid
    row, col = find_S_coordinates()
    s_pipe = pipe_grid[row][col]
    row_len = len(pipe_grid)
    col_len = len(pipe_grid[0])

    checks = []

    if row != row_len - 1:
        checks.append((row + 1, col, "south"))
    if row != 0:
        checks.append((row - 1, col, "north"))
    if col != col_len - 1:
        checks.append((row, col + 1, "east"))
    if col != 0:
        checks.append((row, col - 1, "west"))

    opposites = {"south": "north", "west": "east", "east": "west", "north": "south"}

    for row, col, dir in checks:
        if not pipe_grid[row][col].directions[opposites[dir]]:
            s_pipe.directions[dir] = False


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


def mark_main_loop():
    global pipe_grid
    # Return the bounds of the pipe loop
    row, col = find_S_coordinates()
    pipe_grid[row][col].is_in_closed_loop = True
    row_len = len(pipe_grid)
    col_len = len(pipe_grid[0])

    # Check from every direction of S
    travel_paths = list()
    if row != row_len - 1:
        travel_paths.append((row + 1, col, "north"))
    if row != 0:
        travel_paths.append((row - 1, col, "south"))
    if col != col_len - 1:
        travel_paths.append((row, col + 1, "east"))
    if col != 0:
        travel_paths.append((row, col - 1, "west"))

    for row, col, from_dir in travel_paths:
        p = pipe_at(row, col)
        if not p.directions[from_dir]:
            continue  # Invalid receiving end

        p.travel_and_mark(row, col, from_dir=from_dir)

    return None


def mark_squeeze_able_passthrough():
    # Mark pipes in the original grid where an animal can squeeze through them
    global pipe_grid
    figure_s_shape()

    copy_grid = [[p if p.is_in_closed_loop else None for p in row] for row in pipe_grid]

    row_len = len(copy_grid)
    col_len = len(copy_grid[0])

    def check_squeeze_ability(row, col) -> bool:
        # Check if two pipes in a closed loop are next to each other and not connected.
        checks = []

        if row != row_len - 1:
            checks.append((row + 1, col))
        if row != 0:
            checks.append((row - 1, col))
        if col != col_len - 1:
            checks.append((row, col + 1))
        if col != 0:
            checks.append((row, col - 1))

        # Get pipe pointers
        checks = [copy_grid[row][col] for row, col in checks]

        checks = filter(lambda pipe: pipe, checks)  # Remove Nones

        if not checks:
            return True  # Technically squeeze-able since nothing is behind it

        checks = filter(lambda pipe: pipe.is_in_closed_loop, checks)

        if not checks:
            return True  # Technically squeeze-able since nothing is behind it

        return not all([copy_grid[row][col].does_connect(other) for other in checks])

    for row in range(row_len):
        for col in range(col_len):
            if not copy_grid[row][col]:
                continue  # Skip if None

            copy_grid[row][col].is_squeeze_through = check_squeeze_ability(row, col)


def flood(grid):
    # Flood starts from borders of grid
    # cell.is_in_closed_loop = True = Pipe from main loop,
    # cell.is_in_closed_loop = False = not in the main loop,
    # cell = None = Flooded cell that was not in the main loop and was traveled through

    row_count = len(grid)
    col_count = len(grid[0])

    # Initial seed
    stack: list = []

    # Add borders
    for row in range(row_count):
        stack.append((row, 0))
        stack.append((row, row_count - 1))

    for col in range(col_count):
        stack.append((0, col))
        stack.append((col_count - 1, col))

    while stack:
        row, col = stack.pop()

        if 0 <= row < row_count and 0 <= col < col_count:
            if not grid[row][col]:
                continue

            tmp: pipe = grid[row][col]
            grid[row][col] = None  # Passed

            if not tmp.is_in_closed_loop:
                # Add neighbors to stack, if they had already been processed, they will be skipped since they are None.
                stack.append((row + 1, col))
                stack.append((row - 1, col))
                stack.append((row, col + 1))
                stack.append((row, col - 1))

            # Handle special case where animal can squeeze between pipes facing different directions
            if tmp.is_squeeze_through:
                # Add neighbors to stack, if they had already been processed, they will be skipped since they are None.
                stack.append((row + 1, col))
                stack.append((row - 1, col))
                stack.append((row, col + 1))
                stack.append((row, col - 1))


def count_falsies(grid) -> int:
    # Check if f is not None and if it is still considered not in a closed loop
    grid = [f for row in grid for f in row if f and f.is_in_closed_loop is False]
    return len(grid)


def part2():
    global pipe_grid

    # Mark main loop.
    mark_main_loop()
    mark_squeeze_able_passthrough()
    main_loop_grid = pipe_grid[:]  # Do not destroy original

    flood(main_loop_grid)

    # Count how many False cells are left in the grid.
    area = count_falsies(main_loop_grid)
    print(f"Area is: {area}")

    return


def main():
    get_pipes()
    part1()  # Solution was 6864
    part2()


if __name__ == "__main__":
    main()
