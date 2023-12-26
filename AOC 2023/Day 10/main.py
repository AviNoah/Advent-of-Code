# Find the shape of a pipe, marked S that will create a closed loop with other pipes surrounding it.

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


def part1():
    pass


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
