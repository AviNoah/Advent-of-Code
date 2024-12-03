with open("input.txt", "r") as f:
    lines: list = f.readlines()

data = [line.strip().split() for line in lines]
data = [[int(item) for item in row] for row in data]


def part1():
    pass


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
