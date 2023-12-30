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
        cols = len(self.universe[0])

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
        results = list()
        for i, galaxy1 in enumerate(self.get_galaxies()):
            for j, galaxy2 in enumerate(self.get_galaxies()):
                if i == j:
                    continue  # Skip self
                results.append(universe.min_pair_dist(galaxy1, galaxy2))

        return results

    def sum_pair_dists(self) -> int:
        # Return the sum of the minimal distances between galaxies:
        # Since we are pairing each galaxy with each other, we are double counting
        # Divide by two to fix this
        pairs: list = self.pairs_dist()
        return sum(pairs) // 2

    def expand(self, value):
        # Expand by value any vertical or horizontal line that is completely devoid of galaxies.
        # Return new resulting universe in a new object
        value = max(value - 1, 1)
        rows = len(self.universe)
        cols = len(self.universe[0])

        result = self.universe.copy()

        row = 0
        while row < rows:
            if all([result[row][col] == "." for col in range(cols)]):
                for _ in range(value):
                    result.insert(row, result[row].copy())  # Double it
                rows += value  # Increase size
                row += value  # Skip double
            row += 1

        rows = len(result)
        cols = len(result[0])

        col = 0
        row = 0
        while col < cols:
            if all([result[row][col] == "." for row in range(rows)]):
                for _ in range(value):
                    [result[row].insert(col, ".") for row in range(rows)]  # Double it
                cols += value  # Increase size
                col += value  # Skip double
            col += 1

        return universe(result)

    def pair_dist_optimized(self, value: int) -> list:
        # Assume we have N rows that are just spaces, this will add N*value vertical dist
        # Notice N does not effect the number of cols that are just spaces, M.
        # The horizontal dist will be added M*value to it

        results = list()
        for i, galaxy1 in enumerate(self.get_galaxies()):
            for j, galaxy2 in enumerate(self.get_galaxies()):
                if i == j:
                    continue  # Skip self
                base_dist = universe.min_pair_dist(galaxy1, galaxy2)
                rows, cols = self.count_empty_rows_and_cols(galaxy1, galaxy2)
                # Calculate new dist in expanded universe
                results.append(base_dist + rows * value + cols + value)

        return results

    def expand_optimized(self, value) -> int:
        # An optimized solution that increases empty rows and cols by value.
        # Return the sum of the values instead of returning a new universe object.

        # Times value means having value - 1 more copies of the object
        value = max(value - 1, 1)
        pairs: list = self.pair_dist_optimized(value)
        # Since we are double counting, divide by 2
        return sum(pairs) // 2

    def count_empty_rows_and_cols(
        self, galaxy1: tuple[int, int], galaxy2: tuple[int, int]
    ) -> tuple[int, int]:
        # Return a tuple containing count of empty rows and count of empty cols between two galaxies

        # Now if we check for the amount of empty rows and cols between every 2 galaxies, and
        # get N and M and the galaxies positions, we can calculate for very large values of value
        # very easily

        r_min, r_max = min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])
        c_min, c_max = min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])

        row_count = 0
        col_count = 0

        row_length = len(self.universe)

        for row in self.universe[r_min : r_max + 1]:
            if "#" not in row:
                row_count += 1

        for col in range(c_min, c_max + 1):
            if all([self.universe[row][col] != "#" for row in range(row_length)]):
                col_count += 1

        return row_count, col_count

    def __str__(self) -> str:
        string = ""
        for row in self.universe:
            string += "".join(row)
            string += "\n"
        return string

    @staticmethod
    def from_lines(lines: list):
        # Return a universe object from lines
        lines = [list(line.replace("\n", "")) for line in lines]
        return universe(lines)

    @staticmethod
    def min_pair_dist(galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
        # Without going diagonally (you can pass through galaxies).
        return abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])


def part1():
    global lines
    uni: universe = universe.from_lines(lines)
    print(f"Before expanding sum is: {uni.sum_pair_dists()}")
    uni = uni.expand(2)
    print(f"After expanding sum is: {uni.sum_pair_dists()}")


def part2():
    global lines
    uni: universe = universe.from_lines(lines)
    print(f"Before expanding sum is: {uni.sum_pair_dists()}")
    # This is obviously the slow way to do this
    # uni = uni.expand(1_000_000)
    uni_sum = uni.expand_optimized(1_000_000)
    uni_sum = uni.expand_optimized(10)
    print(f"After expanding sum is: {uni_sum}")


def main():
    part1()  # Ans was 9545480
    part2()


if __name__ == "__main__":
    main()
