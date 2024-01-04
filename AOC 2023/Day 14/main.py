# The rounded rocks (O) will roll when the platform is tilted,
# while the cube-shaped rocks (#) will stay in place, empty spaces are marked (.)
# You may tilt in all 4 directions

# To calculate the load on a support beam in a direction we do this:
# The amount of load caused by a single rounded rock (O) is equal to the number of rows
# from the rock to the other edge of the platform, including the row the rock is on.
# square rocks dont add load.

# Find the total load on the north support beam

with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()


class stone_grid:
    def __init__(self, grid) -> None:
        self.grid = grid

    def tilt(self, direction):
        # Move all round rocks as far as you can in the direction given.
        ...

    def calculate_load(self, direction) -> int:
        # Calculate load on the beam in the given direction
        ...

    def __str__(self) -> str:
        return "\n".join(self.grid)


def part1():
    pass


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
