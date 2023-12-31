# Input contains rows of springs, '.' means operational, '#' means damaged, '?' is unknown.
# immediately after there is a list of the size of each contiguous group of DAMAGED springs

# Equipped with this information, it is your job to figure out how many different
# arrangements of operational and broken springs fit the given criteria in each row.

# Sum counts of all possible arrangements for every row

import re
from math import comb

broken_pattern = r"#+"
broken_pattern: re.Pattern = re.compile(broken_pattern)

missing_pattern = r"\?+"
missing_pattern: re.Pattern = re.compile(missing_pattern)

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class spring_row:
    def __init__(self, operational_data: str, contiguous_data: list) -> None:
        self.operational: str = operational_data
        self.contiguous: list = contiguous_data

    def count_variations(self) -> int:
        global broken_pattern, missing_pattern
        broken_matches: list[re.match] = broken_pattern.finditer(self.operational)
        missing_matches: list[re.match] = missing_pattern.finditer(self.operational)

        # Extract start index and len from each
        broken_matches: list[int, int] = [
            (match.start(), match.end() - match.start()) for match in broken_matches
        ]
        missing_matches: list[int, int] = [
            (match.start(), match.end() - match.start()) for match in missing_matches
        ]

        tmp_contiguous = self.contiguous.copy()

        # TODO: check if maybe you need to multiply the combinatorics
        count = 0

        # While there are broken matches or more broken potential parts and missing matches
        while tmp_contiguous:
            if not missing_matches:
                # Rest must be from broken_matches, break.
                break

            # Check if broken matches is empty or if missing match comes before it
            if not broken_matches or missing_matches[0][0] < broken_matches[0][0]:
                # Complex case, varying cases, start counting here
                index, length = missing_matches.pop(0)
                # If tmp is less than contiguous[0], set to zero and readd to missing.
                diff = length - tmp_contiguous[0]

                if diff == 0:
                    # Simple case, all question marks went into tmp_contiguous
                    # Do not add to count, only one way
                    tmp_contiguous[0] = 0

                if diff < 0:
                    # Not enough to fill with missing match, give it all.
                    # Add to count the amount of ways to choose length in tmp_contiguous[0]
                    count += comb(tmp_contiguous[0], length)
                    tmp_contiguous[0] -= length

                if diff > 0:
                    # Too many, remove first element of contiguous and
                    # readd missing element to start and delegate to next loop.
                    # NOTE: this means the contiguous sequence was broken and at least 1 .
                    # must appear immediately at the end of the tmp_contiguous[0] steps.
                    # therefore another 1 is deducted from length

                    # Do not add to count, only one way
                    index += (
                        tmp_contiguous[0] + 1
                    )  # move ahead tmp_contiguous[0] steps + 1 functional spring
                    length -= (
                        tmp_contiguous[0] + 1
                    )  # Subtract tmp_contiguous[0] steps  + 1 functional spring
                    missing_matches.insert(0, (index, length))
                    tmp_contiguous[0] = 0

            else:
                # Simplest case, feed broken into contiguous
                tmp_contiguous[0] -= broken_matches.pop(0)[1]

            if tmp_contiguous[0] == 0:
                tmp_contiguous.pop(0)

        return max(count, 1)  # If no variations found, return 1 at minimum.

    def __str__(self) -> str:
        return self.operational + " " + ",".join(self.contiguous)

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
            # Keep op_data as string.
            cont_data = cont_data.split(",")
            # Turn to int
            cont_data = list(map(lambda num: int(num), cont_data))

            return spring_row(op_data, cont_data)

        return [extract(line) for line in lines]


def part1():
    spring_rows: list[spring_row] = spring_row.from_lines()
    arrangements = [sp.count_variations() for sp in spring_rows]
    total = sum(arrangements)
    print(f"{total=}")

    for spring, arrangement in zip(spring_row, arrangements):
        print(f"{spring} - {arrangement=}")


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
