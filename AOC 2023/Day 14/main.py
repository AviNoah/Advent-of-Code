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
    def __init__(self, grid: list[list]) -> None:
        self.grid: list[list] = grid

    def get_line(self, direction, at) -> list:
        # return the line in the direction given
        if direction == "north" or direction == "south":
            # at represents column
            return [row[at] for row in self.grid]
        # at represents row
        return self.grid[at].copy()

    def tilt(self, direction):
        # Move all round rocks as far as you can in the direction given.
        # For now implement only if the direction is north
        if direction == "north" or direction == "south":
            # Since we are moving the entire line, other lines should not interfere
            # do columns
            for at in range(len(self.grid[0])):
                self.tilt_line(direction, at)
        elif direction == "west" or direction == "east":
            # Since we are moving the entire line, other lines should not interfere
            # Do rows
            for at in range(len(self.grid)):
                self.tilt_line(direction, at)

    def tilt_line(self, direction, at):
        line: list = self.get_line(direction, at)
        ...

    def count_round_rocks_at(self, line: list) -> list:
        # Return a list of the amount of O's between square rocks
        count_of_O = list()
        while line:
            try:
                i = line.index("#")
                count_of_O.append(line[:i].count("O"))
                line = line[i + 1 :]

            except ValueError:
                # No square rocks left
                count_of_O.append(line.count("O"))
                line = []

        return count_of_O

    def calculate_load(self, direction) -> int:
        # Calculate load on the beam in the given direction
        # For now implement only if the direction is north

        circles: list[tuple] = self.get_circular_rocks()
        total = 0

        while circles:
            total += self.calculate_load_one(direction, *circles.pop())

        return total

    def calculate_load_one(self, direction, row, col) -> int:
        # Calculate the load one circular rock creates on a direction
        # The load of one rock is the amount of rows or cols from it to the direction given,
        # including the one it is on.
        if direction == "north":
            return row + 1
        else:
            raise Exception(f"{direction} has not been implemented")

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self.grid])

    @staticmethod
    def from_lines():
        # Return stone_grid object from lines
        global lines
        grid: list[list] = [list(row.replace("\n", "")) for row in lines]

        return stone_grid(grid)


def part1():
    grid = stone_grid.from_lines()
    print(grid)
    print()
    grid.tilt("north")
    print(grid)
    print()
    north_load = grid.calculate_load("north")
    print(f"Load on north beam: {north_load}")


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
