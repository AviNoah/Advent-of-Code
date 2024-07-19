from typing import Literal

with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()
    lines = [line.strip() for line in lines]


directions = Literal["north", "south", "west", "east"]

rock_types = Literal["O", "#"]


class Rock:
    def __init__(self, row: int, col: int, type: rock_types) -> None:
        self.row = row
        self.col = col
        self.type = type


class StoneGrid:

    def __init__(self, grid: list[list]) -> None:
        self.grid = grid
        self.row_count = len(grid)
        self.col_count = len(grid[0])

    def pickup_rocks(self) -> list[Rock]:
        "Pick up all rocks (O) or (#), store their location and type in Rock, mark them as (.) on the grid"
        rocks: list[Rock] = []
        for row in range(self.row_count):
            for col in range(self.col_count):
                rock_type: rock_types = self.grid[row][col]
                if rock_type == "O" or rock_type == "#":
                    rocks.append(Rock(row, col, rock_type))
                    self.grid[row][col] = "."

        return rocks

    def spin_cycle(self) -> None:
        "Tilt north, west, south then east"
        self.tilt("north")
        self.tilt("west")
        self.tilt("south")
        self.tilt("east")

    def tilt(self, dir: directions) -> None:
        """
        Move all rounded rocks (O) in the given direction.
        A rounded rock can move if the next cell is a (.).
        It cannot cross the borders of the grid.

        Square rocks (#) cannot move.

        Args:
            dir (directions): The direction to move the rocks.
        """
        rocks: list[Rock] = self.pickup_rocks()

        match dir:
            case "east":
                tilt_func = self._tilt_east
            case "north":
                tilt_func = self._tilt_north
            case "south":
                tilt_func = self._tilt_south
            case "west":
                tilt_func = self._tilt_west
            case _:
                raise ValueError()

        tilt_func(rocks)

    def _tilt_north(
        self,
        rocks: list[Rock],
    ) -> None:
        for col in range(self.col_count):
            relevant_rocks = [rock for rock in rocks if rock.col == col]
            # Sort by row asc
            sorted_rocks = sorted(
                relevant_rocks, key=lambda rock: rock.row, reverse=False
            )

            free_spot = 0
            for rock in sorted_rocks:
                if rock.type == "#":
                    self.grid[rock.row][col] = "#"
                    free_spot = rock.row + 1

                elif rock.type == "O":
                    self.grid[free_spot][col] = "O"
                    free_spot += 1

    def _tilt_south(
        self,
        rocks: list[Rock],
    ) -> None:
        for col in range(self.col_count):
            relevant_rocks = [rock for rock in rocks if rock.col == col]
            # Sort by row desc
            sorted_rocks = sorted(
                relevant_rocks, key=lambda rock: rock.row, reverse=True
            )

            free_spot = self.col_count - 1
            for rock in sorted_rocks:
                if rock.type == "#":
                    self.grid[rock.row][col] = "#"
                    free_spot = rock.row - 1

                elif rock.type == "O":
                    self.grid[free_spot][col] = "O"
                    free_spot -= 1

    def _tilt_east(
        self,
        rocks: list[Rock],
    ) -> None:
        for row in range(self.row_count):
            relevant_rocks = [rock for rock in rocks if rock.row == row]
            # Sort by col desc
            sorted_rocks = sorted(
                relevant_rocks, key=lambda rock: rock.col, reverse=True
            )

            free_spot = self.row_count - 1
            for rock in sorted_rocks:
                if rock.type == "#":
                    self.grid[row][rock.col] = "#"
                    free_spot = rock.col - 1

                elif rock.type == "O":
                    self.grid[row][free_spot] = "O"
                    free_spot -= 1

    def _tilt_west(
        self,
        rocks: list[Rock],
    ) -> None:
        for row in range(self.row_count):
            relevant_rocks = [rock for rock in rocks if rock.row == row]
            # Sort by col asc
            sorted_rocks = sorted(
                relevant_rocks, key=lambda rock: rock.col, reverse=False
            )

            free_spot = 0
            for rock in sorted_rocks:
                if rock.type == "#":
                    self.grid[row][rock.col] = "#"
                    free_spot = rock.col + 1

                elif rock.type == "O":
                    self.grid[row][free_spot] = "O"
                    free_spot += 1

    def calculate_load(self, dir: directions) -> int:
        """
        The amount of load caused by a single rounded rock (O) is equal to the
        number of rows from the rock to the south edge of the platform, including the row the rock is on.
        Cube-shaped rocks (#) don't contribute to load.

        Args:
            dir (directions): Direction to calculate

        Returns:
            int: Load
        """
        load = 0
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.grid[row][col] == "O":
                    load += self._calculate_load_one_rock(row, col, dir)
        return load

    def _calculate_load_one_rock(self, row: int, col: int, dir: directions) -> int:
        "Calculate the load a circulate rock (O) creates at row, column at given dir"
        match dir:
            case "west":
                return self.col_count - col
            case "south":
                return row + 1
            case "north":
                return self.row_count - row
            case "east":
                return col + 1
            case _:
                raise ValueError()

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self.grid])

    def __repr__(self) -> str:
        return self.__str__()


def from_lines() -> StoneGrid:
    global lines
    return StoneGrid([list(line) for line in lines])


def part1() -> None:
    grid: StoneGrid = from_lines()
    # print(grid)
    grid.tilt("north")
    # print()
    # print(grid)

    north_load = grid.calculate_load("north")
    # print(f"Load on north beam: {north_load}")


def part2() -> None:
    grid: StoneGrid = from_lines()
    cycles = 1000000000
    for cycle in range(cycles):
        grid.spin_cycle()

    north_load = grid.calculate_load("north")
    print(f"Load on north beam: {north_load}")


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
