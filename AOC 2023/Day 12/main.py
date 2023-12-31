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
                # TODO: handle what happens if ? is not used to show a broken machine, yet skips to next one
                index, length = missing_matches.pop(0)
                # If tmp is less than contiguous[0], set to zero and readd to missing.
                diff = length - tmp_contiguous[0]

                if diff == 0:
                    # Simple case, all question marks went into tmp_contiguous
                    # Do not add to count, only one way
                    tmp_contiguous[0] = 0

                if diff < 0:
                    # Not enough to fill with missing match, give it all.
                    # Add to count of the amount of ways to place length in tmp_contiguous[0]
                    # The calculation for that is tmp_contiguous[0] - length choose length
                    count += comb(tmp_contiguous[0] - length, length)
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

    def count(self) -> int:
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

        def recursive_helper(
            contiguous: list, b_matches: list, m_matches: list, is_contiguous: bool
        ) -> int:
            # if is_contiguous, feed must start at start of missing match
            # if not, it may start anywhere.
            if not m_matches:
                # If it is empty, no need to continue
                return 1

            if b_matches and b_matches[0] < m_matches[0]:
                # Forced to subtract from contiguous
                _, length = b_matches.pop()
                if length == contiguous[0]:
                    # Not contiguous
                    contiguous.pop(0)
                    return recursive_helper(contiguous, b_matches, m_matches, False)

                # Length can only be smaller than contiguous
                # Is contiguous
                contiguous[0] -= length
                return recursive_helper(contiguous, b_matches, m_matches, True)

            ...

    def count2(self) -> int:
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

        # Strategy:
        """
        contiguous feed is the first element of the contiguous list
        while contiguous list is not empty:
            if there are no missing_matches:
                rest are broken_matches, break, do not add to count.
                break from while loop.
            
            # There are missing matches
            if there are broken_matches and broken_match starts before missing match:
                pop broken match
                if its length bigger or equal to contiguous feed:
                    # should never be bigger than.
                    deduct its length from contiguous feed
                else:  # It is smaller
                    # The immediate next missing match MUST start with the rest of the feed.
                    # Assume there must be a missing match immediately after.
                    pop missing match, it must begin the sequence, follow three scenarios 
                    below in else
                
            else:
                pop missing match
                # We may choose to add or not to add the length of match into the feed,
                # therefore count of choices increases by 2.
                choose not to use:
                    count += 1  # The option to just not used the feed, the 2nd will be added later
            
                choose to use:
                    # We have three scenarios:
                    - length of match is less than feed:
                        # Add 1, we use the entire length of match
                        subtract length of match from feed
                        count += 1
                    - length of match is exactly the feed:
                        set feed to 0
                        use entire feed
                    - length of match is more than feed:
                        add to count number of ways to insert feed into length of match,
                        which is feed choose length
                        
                        # We now split paths, depending on where we choose to insert this feed,
                        # we create many more possibilities, fill start with working springs
                        and fill the very next spot after our insert with a working spring since we broke
                        contiguity.
                    
            
            if contiguous feed is 0:
                pop it.
        
        """

    def __str__(self) -> str:
        return (
            self.operational
            + " "
            + ",".join(list(map(lambda integer: str(integer), self.contiguous)))
        )

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

    for spring, arrangement in zip(spring_rows, arrangements):
        print(f"{spring} - {arrangement=}")


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
