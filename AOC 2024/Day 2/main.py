with open("input.txt", "r") as f:
    lines: list = f.readlines()

data = [line.strip().split() for line in lines]
data = [[int(item) for item in row] for row in data]


def part1():
    def is_safe(row):
        # Needs to be all increasing or all decreasing
        # Needs to differ by 1,2 or 3 only between adjacent levels
        is_ascending = None
        old = None

        for num in row:
            if old is None:
                old = num
                continue
            if is_ascending is None:
                is_ascending = num > old

            diff = num - old

            if (is_ascending and diff < 0) or (not is_ascending and diff > 0):
                return False

            if not (1 <= abs(diff) <= 3):
                return False

            old = num
        return True

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

    def is_dist_safe(dist, is_asc):
        if dist > 0 and not is_asc:
            return False
        if not (1 <= abs(dist) <= 3):
            return False
        return True

    def is_safe(row):
        # Needs to be all increasing or all decreasing
        # Needs to differ by 1,2 or 3 only between adjacent levels
        # Can have 1 unsafe

        dists = []
        for i in range(len(row) - 1):
            dists.append(row[i + 1] - row[i])

        is_asc = dists[0] > 0
        i = 0
        while i < len(dists) - 1:
            if not is_dist_safe(dists[i], is_asc):
                pass

            i += 1
        return True

    count = 0
    for row in data:
        if is_safe(row):
            count += 1

    return count


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
