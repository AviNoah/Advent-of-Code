import re
from math import comb


with open("input.txt", "r") as f:
    lines: list = f.readlines()


class spring_row:
    def __init__(self, operational_data: str, contiguous_data: list) -> None:
        self.operational: str = operational_data
        self.contiguous: list = contiguous_data

    def count(self) -> int:
        # Return to index in stack, stack contains index and copy of contiguous
        stack = [(0, self.contiguous.copy())]
        c = 0

        while stack:
            is_still_open: bool = False
            head, data = stack.pop()
            for i in range(head, len(self.operational)):
                # Deciding counter - this will do the counting
                if not data:
                    # Check if there are any # left
                    c += 1 if "#" not in self.operational[i:] else 0

                symbol: str = self.operational[i]
                if symbol == ".":
                    if not is_still_open:
                        continue  # Skip.

                    # Check to see if we actually finished the sequence, if not then invalid arrangement
                    if data[0] != 0:
                        break

                    # Valid, continue
                    is_still_open = False  # Close.
                    continue

                # Check to see if we actually already finished the sequence, if yes then invalid arrangement
                if data[0] == 0:
                    break

                if symbol == "#":
                    is_still_open = True
                    data[0] -= 1
                    continue

                # Use the stack to open new starting points
                if symbol == "?":
                    if not is_still_open:
                        # We can choose to not add this as a broken spring
                        stack.append((i + 1, data.copy()))  # Don't add

                    is_still_open = True
                    # Append as broken_spring
                    data[0] -= 1
                    stack.append((i + 1, data.copy()))

        return max(1, c)

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
