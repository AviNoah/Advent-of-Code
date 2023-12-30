# Figure out the sum of the lengths of the shortest path between every
# pair of galaxies
# Due to something involving gravitational effects, only some space expands.
# In fact, the result is that any rows or columns that contain no galaxies should
# all actually be twice as big horizontally and vertically.

from math import comb  # To calculate count of pairs

with open("input.txt", "r") as f:
    lines: list = f.readlines()


def pair_count(galaxies: tuple[int, int]) -> int:
    return comb(galaxies, 2)


def min_pair_dist(galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
    # Without going diagonally (you can pass through galaxies).
    return abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])


def pairs_dist(galaxies: list[tuple[int, int]]) -> list:
    # Given a list of galaxies' positions, return the minimal path between each of them
    ...


def part1():
    pass


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
