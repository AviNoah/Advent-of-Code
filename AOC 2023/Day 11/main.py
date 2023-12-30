# Figure out the sum of the lengths of the shortest path between every
# pair of galaxies
# Due to something involving gravitational effects, only some space expands.
# In fact, the result is that any rows or columns that contain no galaxies should
# all actually be twice as big horizontally and vertically.

from math import comb  # To calculate count of pairs

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class universe:
    def __init__(self, grid) -> None:
        self.universe: list[list] = grid

    def get_galaxies(self) -> list[tuple[int, int]]:
        # Return a list of galaxies locations
        rows = len(self.universe)
        cols = len(self.universe)

        result = [
            (row, col)
            for col in range(cols)
            for row in range(rows)
            if self.universe[row][col] == "#"
        ]
        return result

    def pair_count(self) -> int:
        return comb(len(self.get_galaxies()), 2)

    def pairs_dist(self) -> list:
        # Given a list of galaxies' positions, return the minimal path between each of them
        ...

    def sum_pair_dists(self) -> int:
        # Return the sum of the minimal distances between galaxies:
        return sum(self.pairs_dist())

    def expand(self):
        # Double any vertical or horizontal line that is completely devoid of galaxies.
        # Return new resulting universe in a new object
        rows = len(self.universe)
        cols = len(self.universe)

        result = self.universe.copy()

        row = 0
        while row < rows:
            if all([result[row][col] == "." for col in range(cols)]):
                result.insert(row, result[row])  # Double it
                rows += 1  # Increase size
                row += 1  # Skip double
            row += 1

        rows = len(result)
        cols = len(result)

        col = 0
        while col < cols:
            if all([result[row][col] == "." for row in range(rows)]):
                [result[row].insert(col, ".") for row in range(rows)]  # Double it
                cols += 1  # Increase size
                col += 1  # Skip double
            col += 1

        return universe(result)

    @staticmethod
    def from_lines(lines: list):
        # Return a universe object from lines
        lines = [line.replace("\n", "").split() for line in lines]
        return universe(lines)

    @staticmethod
    def min_pair_dist(galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
        # Without going diagonally (you can pass through galaxies).
        return abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])


def part1():
    pass


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
