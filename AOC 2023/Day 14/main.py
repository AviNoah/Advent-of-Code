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
        # For now implement only if the direction is north
        circles: list[tuple] = list(
            [
                (i, j)
                for i, row in enumerate(self.stone_grid)
                for j, elem in enumerate(row)
                if row == "O"
            ]
        )

        while circles():
            self.tilt_one(direction, *circles.pop())

    def tilt_one(self, direction, row, col):
        # Tilt a single circular stone towards direction
        if direction == "north":
            ...

        else:
            raise Exception(f"{direction} has not been implemented")

    def calculate_load(self, direction) -> int:
        # Calculate load on the beam in the given direction
        # For now implement only if the direction is north
        if direction == "north":
            ...
        else:
            raise Exception(f"{direction} has not been implemented")

    def __str__(self) -> str:
        return "\n".join(self.grid)

    @staticmethod
    def from_lines():
        # Return stone_grid object from lines
        global lines
        grid: list[str] = [row.replace("\n", "") for row in lines]

        return stone_grid(grid)


def part1():
    grid = stone_grid.from_lines()
    print(grid)
    pass


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
