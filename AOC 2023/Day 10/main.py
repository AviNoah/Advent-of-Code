# Find the shape of a pipe, marked S that will create a closed loop with other pipes surrounding it.
# Afterwards, walk along the loop and find the farthest pipe from it.

# Strategy - measure how far every pipe is from S, if two paths join at the SAME distance value, they
# MUST close a loop. this way we find the farthest point AND the main loop.

with open("input.txt", "r") as f:
    lines: list = f.readlines()

pipe_types: dict = {
    "|": "north-south",
    "-": "east-west",
    "L": "north-east",
    "J": "north-west",
    "7": "south-west",
    "F": "south-east",
    ".": "ground",  # No pipe
    "S": "start",  # Unknown pipe
}


class pipe:
    def __init__(self, symbol: str):
        self.symbol: str = symbol
        self.type: str = pipe_types.get(symbol, "ground")

        self.from_card = None
        self.to_card = None
        cardinals = self.type.split("-")
        if len(cardinals) == 2:
            self.from_card, self.to_card = cardinals


def get_pipes() -> list[pipe]:
    global lines

    def pipes_from_line(line: str) -> list[pipe]:
        line: str = line.replace("\n", "")
        return [pipe(char) for char in line]

    table = [pipes_from_line(line) for line in lines]
    return table


def part1():
    pipes: pipe = get_pipes()


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
