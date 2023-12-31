# Input contains rows of springs, '.' means operational, '#' means damaged, '?' is unknown.
# immediately after there is a list of the size of each contiguous group of DAMAGED springs

# Equipped with this information, it is your job to figure out how many different
# arrangements of operational and broken springs fit the given criteria in each row.

# Sum counts of all possible arrangements for every row

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class spring_row:
    def __init__(self, operational_data: list, contiguous_data: list) -> None:
        self.operational: list = operational_data
        self.contiguous: list = contiguous_data

    @staticmethod
    def from_lines() -> list:
        # Return list of spring_row objects from lines
        global lines

        def extract(line: str) -> spring_row:
            line = line.replace("\n", "")
            line: list = line.split(" ", maxsplit=1)
            if len(line) == 1:
                # in case all springs are operational - no contiguous data
                line.append(list())

            # length of line is 2
            op_data, cont_data = line
            op_data = list(op_data)  # Make into a list.
            cont_data = cont_data.split(",")

            return spring_row(op_data, cont_data)

        return [extract(line) for line in lines]


def part1():
    pass


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
