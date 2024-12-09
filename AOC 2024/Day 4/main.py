with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def part1():
    # Find all x's and search in all 8 directions
    global lines
    dirs = [
        (1, 0, 1),  # X Y index of xmas word
        (-1, 0, 1),
        (0, 1, 1),
        (0, -1, 1),
        (1, 1, 1),
        (-1, 1, 1),
        (-1, -1, 1),
        (1, -1, 1),
    ]

    count = 0
    word = "XMAS"
    ROWS = len(lines)
    COLS = len(lines[0])

    for i in range(ROWS):
        for j in range(COLS):
            if lines[i][j] != word[0]:
                continue

            dir_stack = dirs.copy()
            while dir_stack:
                x_diff, y_diff, xmas_index = dir_stack.pop()

                if i + x_diff >= ROWS or j + y_diff >= COLS:
                    continue

                if lines[i + x_diff][j + y_diff] == word[xmas_index]:
                    xmas_index += 1
                    if xmas_index == len(word):
                        count += 1
                    else:
                        dir_stack.append((i + x_diff, j + y_diff, xmas_index))

    return count


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
