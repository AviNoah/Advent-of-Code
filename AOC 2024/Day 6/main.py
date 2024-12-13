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


def advance(orig_row, orig_col, facing) -> tuple | None:
    "Return the guards next position and direction, if exits, return None"
    new_row, new_col = get_next_location(orig_row, orig_col, facing)
    if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
        return None  # Left bounds

    if grid[new_row][new_col] == "#":
        return orig_row, orig_col, rotate_face(facing)

    return new_row, new_col, facing


def part1():
    global grid, ROWS, COLS
    row, col = get_guard_pos(grid)
    facing = "up"

    # Guard spawn point is visited
    grid[row][col] = "X"
    count = 1

    while (result := advance(row, col, facing)) is not None:
        row, col, facing = result

        if grid[row][col] != "X":
            count += 1
        # Mark that the guard stood there
        grid[row][col] = "X"

    return count


def main():
    # part1()
    # part2()
    pass


if __name__ == "__main__":
    main()
