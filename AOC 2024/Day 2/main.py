with open("input.txt", "r") as f:
    lines: list = f.readlines()

data = [line.strip().split() for line in lines]
data = [[int(item) for item in row] for row in data]


def is_safe(row):
    diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    are_asc = [diff > 0 for diff in diffs]
    within_range = [1 <= abs(diff) <= 3 for diff in diffs]

    same_order = all(are_asc) or not any(are_asc)
    all_within_range = all(within_range)

    return all_within_range and same_order


def part1():
    global data
    count = 0
    for row in data:
        if is_safe(row):
            count += 1

    return count


def part2():

    # Some examples that can be tolerated
    # 1 5 6 8
    # 1 2 7 9
    # 1 2 2 3
    global data

    def dampen(row):
        # Horrible first solution just to get the thing working
        if is_safe(row):
            return True

        for i in range(len(row)):
            if is_safe(row[:i] + row[i + 1 :]):
                return True
        return False

    count = 0
    for row in data:
        if dampen(row):
            count += 1

    return count


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
