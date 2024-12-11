with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()
    grid: list[list] = [list(line.strip()) for line in lines]
    ROWS = len(grid)
    COLS = len(grid[0])


def get_guard_pos(grid):
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] not in {".", "#"}:
                return row, col


def part1():
    global grid, ROWS, COLS
    row, col = get_guard_pos(grid)
    facing = "up"
    count = 0

    while 0 <= row < ROWS and 0 <= col < COLS:
        if grid[row][col] != "X":
            count += 1
        # Mark that the guard stood there
        grid[row][col] = "X"
        try:
            match facing:
                case "up":
                    row -= 1
                    if grid[row][col] == "#":
                        facing = "right"
                        row += 1
                case "down":
                    row += 1
                    if grid[row][col] == "#":
                        facing = "left"
                        row -= 1
                case "right":
                    col += 1
                    if grid[row][col] == "#":
                        facing = "down"
                        col -= 1
                case "left":
                    col -= 1
                    if grid[row][col] == "#":
                        facing = "up"
                        col += 1
        except IndexError:
            pass

    return count


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
