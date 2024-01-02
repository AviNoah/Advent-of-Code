# Given patterns of rocks . and ash #, figure out where the mirror is.
# Each land data has one mirror in it.
# A mirror is vertical or horizontal, it will reflect the data along it perfectly,
# it can be placed not in the middle too, meaning one side will have more information than the other,
# but the side with less information will match the other exactly up until that point.
# vertical - mirror is exactly between two columns
# horizontal - mirror is exactly between two rows

# Add number of columns to the left of each vertical mirror, with 100 multiplied by
# the number of rows above each horizontal mirror.

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class land_data:
    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data
        self.data_inverted: list[str] = self.invert_rows_and_cols()

    def invert_rows_and_cols(self) -> list[str]:
        # Invert rows and columns between each other.
        new_data: list[str] = []
        for i in range(len(self.data[0])):
            new_data.append("".join([row[i] for row in self.data]))

        return new_data

    def get_horizontal_mirror(self) -> int:
        # Find horizontal mirror
        for i, row in enumerate(self.data):
            for j, other in enumerate(self.data):
                if i == j:
                    continue
                if row == other:
                    lower = (i + j) // 2
                    # Verify they all equal one another
                    if self.test_range(lower, lower + 1, self.data):
                        return lower + 1

        return None

    def get_vertical_mirror(self) -> int:
        # Find vertical mirror
        for i, col in enumerate(self.data_inverted):
            for j, other in enumerate(self.data_inverted):
                if i == j:
                    continue
                if col == other:
                    lower = (i + j) // 2
                    # Verify they all equal one another
                    if self.test_range(lower, lower + 1, self.data_inverted):
                        return lower + 1

        return None

    def get_mirrors(self) -> tuple[int, int]:
        # Return the count of columns left to the vertical mirror and the count of
        # rows above the horizontal mirror
        vertical = self.get_vertical_mirror()
        horizontal = self.get_horizontal_mirror()

        vertical = vertical if vertical else 0
        horizontal = horizontal if horizontal else 0

        return vertical, horizontal

    def __str__(self) -> str:
        return "\n".join(self.data)

    @staticmethod
    def test_range(lower, upper, grid) -> bool:
        # Test if all rows from lower and above to upper and below are equal to one another
        rng = range(min((len(grid) - upper - 1), lower))

        return all([grid[lower - i - 1] == grid[upper + i + 1] for i in rng])

    @staticmethod
    def get_lands() -> list:
        global lines
        lands = []
        land = []
        for line in lines:
            line = line.replace("\n", "")
            if line == "":
                lands.append(land)
                land = []
                continue

            land.append(line)
        else:
            lands.append(land)
            land = []

        lands: list[land_data] = [land_data(land) for land in lands]
        return lands


def part1():
    lands: list[land_data] = land_data.get_lands()
    mirrors: list[tuple] = [land.get_mirrors() for land in lands]

    total = sum(mirror[0] + (mirror[1] * 100) for mirror in mirrors)
    print(f"Sum is: {total}")


def part2():
    pass


def main():
    part1()  # Prev ans was 37619
    part2()


if __name__ == "__main__":
    main()
