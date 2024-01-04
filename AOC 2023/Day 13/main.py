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

    def invert_rows_and_cols_of_inverted_data(self) -> list[str]:
        # Invert rows and columns between each other.
        new_data: list[str] = []
        for i in range(len(self.data_inverted[0])):
            new_data.append("".join([row[i] for row in self.data_inverted]))

        return new_data

    def get_horizontal_mirror(self, ignore_row: int = -1) -> int:
        # Find horizontal mirror

        for i in range(len(self.data) - 1):
            if ignore_row == i:
                continue

            # Verify they all equal one another
            if all(self.test_range(i, i + 1, self.data)):
                return i + 1

        return 0

    def get_vertical_mirror(self, ignore_col: int = -1) -> int:
        # Find vertical mirror

        for i in range(len(self.data_inverted) - 1):
            if ignore_col == i:
                continue

            # Verify they all equal one another
            if all(self.test_range(i, i + 1, self.data_inverted)):
                return i + 1

        return 0

    def get_mirrors(self, fix_smudges) -> tuple[int, int]:
        # Return the count of columns left to the vertical mirror and the count of
        # rows above the horizontal mirror

        vertical = self.get_vertical_mirror()
        horizontal = self.get_horizontal_mirror()

        if not fix_smudges:
            return vertical, horizontal

        # Run again with fixed mirrors, find a DIFFERENT reflection line
        self.fix_mirrors()

        vertical_fixed = self.get_vertical_mirror(ignore_col=vertical - 1)
        horizontal_fixed = self.get_horizontal_mirror(ignore_row=horizontal - 1)

        if vertical_fixed != 0 or horizontal_fixed != 0:
            # Remove old one
            vertical_fixed = vertical_fixed if vertical_fixed != vertical else 0
            horizontal_fixed = horizontal_fixed if horizontal_fixed != horizontal else 0

        else:
            raise Exception("No new mirror found! there has to be a new mirror.")

        return vertical_fixed, horizontal_fixed

    def fix_horizontal_mirror(self):
        # Return whether a horizontal mirror was fixed or not.

        for i in range(len(self.data) - 1):
            # Check if there is only 1 difference from a full reflection
            if self.test_smudge(i, i + 1, self.data):
                # Update inverted data
                self.data_inverted = self.invert_rows_and_cols()
                return True
        return False

    def fix_vertical_mirror(self):
        # Return whether a horizontal mirror was fixed or not.

        for i in range(len(self.data_inverted) - 1):
            # Check if there is only 1 difference from a full reflection
            if self.test_smudge(i, i + 1, self.data_inverted):
                # Update data
                self.data = self.invert_rows_and_cols_of_inverted_data()
                return True

        return False

    def fix_mirrors(self):
        # Remove smudges from mirror
        # We must fix the smudge and THEN check for reflection line
        # We must find a reflection that is one smudge away from being valid.
        # Only one mirror can have a smudge.

        if self.fix_horizontal_mirror():
            return

        self.fix_vertical_mirror()

    def __str__(self) -> str:
        return "\n".join(self.data)

    @staticmethod
    def test_smudge(lower, upper, grid) -> bool:
        # Find a smudge and fix it and return true if found, return false otherwise

        boolean_check: list[bool] = land_data.test_range(lower, upper, grid)

        # Check if there is only 1 false in boolean_check, at that i, we must check if the patterns differ
        # by one character.
        if boolean_check.count(False) != 1:
            return False  # Invalid mirror

        # This row is i steps away from lower side of mirror. (Excluding lower side)
        steps = boolean_check.index(False)

        underside: list = list(grid[lower - steps])
        upside: list = list(grid[upper + steps])

        # Check if they differ by one symbol
        check_letters: list = [r == o for r, o in zip(underside, upside)]

        if check_letters.count(False) != 1:
            # There should be only 1 smudge, invalid mirror smudge
            return False

        # Invert the data at the smudge point, return new reflection line
        col = check_letters.index(False)
        underside[col] = "#" if underside[col] == "." else "."
        new_row = "".join(underside)

        grid[lower - steps] = new_row  # Update grid
        return True  # Smudge found

    @staticmethod
    def test_range(lower, upper, grid) -> list[bool]:
        # Test if all rows from lower and above to upper and below are equal to one another
        rng = range(min((len(grid) - upper), lower + 1))

        boolean_check: list[bool] = [grid[lower - i] == grid[upper + i] for i in rng]

        return boolean_check

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


def part1(fix_smudges: bool = False):
    lands: list[land_data] = land_data.get_lands()
    mirrors: list[tuple] = [land.get_mirrors(fix_smudges) for land in lands]

    total = sum(mirror[0] + (mirror[1] * 100) for mirror in mirrors)
    print(f"Sum is: {total}")


def part2():
    part1(fix_smudges=True)


def main():
    # part1()  # Ans was 30705
    part2()


if __name__ == "__main__":
    main()
