import re

with open("input.txt", "r") as f:
    data = f.read()


def part1():
    global data
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    for match in pattern.finditer(data):
        total += int(match.group(1)) * int(match.group(2))

    return total


def part2():
    global data
    temp_data = data

    parts = temp_data.split("do()")
    parts = [part.split("don't()")[0] for part in parts]
    usable = "".join(parts)

    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0
    for match in pattern.finditer(usable):
        total += int(match.group(1)) * int(match.group(2))

    return total


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
