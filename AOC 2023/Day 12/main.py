# Input contains rows of springs, '.' means operational, '#' means damaged, '?' is unknown.
# immediately after there is a list of the size of each contiguous group of DAMAGED springs

# Equipped with this information, it is your job to figure out how many different
# arrangements of operational and broken springs fit the given criteria in each row.

# Sum counts of all possible arrangements for every row

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class spring_row:
    def __init__(self, operational_data: str, contiguous_data: list) -> None:
        self.operational: str = operational_data
        self.contiguous: list = contiguous_data

    def count(self) -> int:
        # Return to index in stack, stack contains index and copy of contiguous
        stack = [(0, self.contiguous.copy(), False)]
        c = 0

        while stack:
            head, data, is_still_open = stack.pop()
            for i in range(head, len(self.operational)):
                # Deciding counter - this will do the counting
                if not data:
                    # Check if there are any # left
                    c += 1 if "#" not in self.operational[i:] else 0
                    break  # End for loop

                symbol: str = self.operational[i]

                # Check if contiguous sequence finished
                if data[0] == 0:
                    # Three scenarios: ., ? or #;   # = Invalid, ? as a # is invalid, so make it .
                    if symbol == "#":
                        break  # Invalid arrangement

                    # Assume the ? is a .
                    data.pop(0)
                    is_still_open = False
                    continue  # Skip it

                # Working spring
                if symbol == ".":
                    if not is_still_open:
                        continue  # Skip.

                    break  # Since we know data[0] is not zero, we have not finished the contiguous sequence

                # Check to see if we actually already finished the sequence, if yes then invalid arrangement

                # Broken spring
                if symbol == "#":
                    is_still_open = True
                    data[0] -= 1
                    continue

                # Use the stack to open new starting points
                # Either broken or working spring two choices
                if symbol == "?":
                    if not is_still_open:
                        # Add as working spring, we may chose so because it is not still open
                        stack.append((i + 1, data.copy(), False))  # Don't add

                    # Continue as broken_spring
                    is_still_open = True
                    data[0] -= 1

            else:
                # Executes only if not stopped by a break
                if not data or (len(data) == 1 and data[0] == 0):
                    # Since we went through the entirety of string, this counts
                    c += 1

        return max(1, c)

    def unfold(self, value):
        # Return a new spring_row object that multiplies self.operational_data by value
        op_data: list = [self.operational] * value
        op_data: str = "?".join(op_data)
        return spring_row(op_data, self.contiguous)

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
    arrangements = [sp.count() for sp in spring_rows]
    total = sum(arrangements)

    for spring, arrangement in zip(spring_rows, arrangements):
        print(f"{spring} - {arrangement=}")

    print(f"{total=}")


def part2():
    # They were all folded, to unfold add 4 copies to each operational data to itself,
    # separated by ?
    spring_rows: list[spring_row] = spring_row.from_lines()
    spring_rows: list[spring_rows] = [row.unfold(5) for row in spring_rows]

    arrangements = [sp.count() for sp in spring_rows]
    total = sum(arrangements)

    for spring, arrangement in zip(spring_rows, arrangements):
        print(f"{spring} - {arrangement=}")

    print(f"{total=}")


def main():
    part1()  # Ans was 7163
    part2()


if __name__ == "__main__":
    main()
