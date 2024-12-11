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


def get_next_location(row, col, facing) -> tuple[int, int]:
    match facing:
        case "up":
            return row - 1, col
        case "down":
            return row + 1, col
        case "right":
            return row, col + 1
        case "left":
            return row, col - 1
    raise


def rotate_face(facing) -> str:
    match facing:
        case "up":
            return "right"
        case "down":
            return "left"
        case "right":
            return "down"
        case "left":
            return "up"
    raise


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

        row1, col1 = get_next_location(row, col, facing)
        try:
            if grid[row1][col1] == "#":
                facing = rotate_face(facing)
            else:
                row, col = row1, col1
        except IndexError:
            # We broke out of bounds - guard exited
            break
    return count


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
