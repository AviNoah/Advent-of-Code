with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def part1():
    # Find all x's and search in all 8 directions
    global lines
    dirs = [
        (1, 0),  # X Y index of xmas word
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, 1),
        (-1, -1),
        (1, -1),
    ]

    count = 0
    word = "XMAS"
    ROWS = len(lines)
    COLS = len(lines[0])

    def search(row, col, row_diff, col_diff, expected):
        global lines
        if expected == len(word):
            return 1

        row += row_diff
        col += col_diff

        if row >= ROWS or col >= COLS or row < 0 or col < 0:
            return 0

        if lines[row][col] != word[expected]:
            return 0
        return search(row, col, row_diff, col_diff, expected + 1)

    for i in range(ROWS):
        for j in range(COLS):
            if lines[i][j] != word[0]:
                continue
            for row_diff, col_diff in dirs:
                count += search(i, j, row_diff, col_diff, 1)

    return count


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
