# Given patterns of rocks . and ash #, figure out where the mirror is.
# A mirror is either vertical or horizontal, it will reflect the data along it perfectly,
# it can be placed not in the middle too, meaning one side will have more information than the other,
# but the side with less information will match the other exactly up until that point.
# vertical - mirror is exactly between two columns
# horizontal - mirror is exactly between two rows

# Add number of columns to the left of each vertical mirror, with 100 multiplied by
# the number of rows above each horizontal mirror.

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class land_data:
    def __init__(self, data: list) -> None:
        self.data = data

    def get_mirror(self) -> tuple[int, int]:
        # Return the two columns or two rows representing mirror location
        # left is lower, right is upper
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
