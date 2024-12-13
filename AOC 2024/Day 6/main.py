with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()
    grid: list[list] = [list(line.strip()) for line in lines]
    ROWS = len(grid)
    COLS = len(grid[0])


def get_guard_pos():
    global grid
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] not in {".", "#"}:
                return row, col


GUARD_ROW, GUARD_COL = get_guard_pos()


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


def advance(orig_row, orig_col, facing) -> tuple[int, int, str] | None:
    "Return the guards next position and direction, if exits, return None"

    new_row, new_col = get_next_location(orig_row, orig_col, facing)
    if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
        return None  # Left bounds

    if grid[new_row][new_col] == "#":
        return orig_row, orig_col, rotate_face(facing)

    return new_row, new_col, facing


def part1():
    global grid, ROWS, COLS, GUARD_COL, GUARD_ROW
    row, col = GUARD_ROW, GUARD_COL
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


def would_loop(orig_row, orig_col, orig_facing) -> bool:
    "Advance using two guards, one faster than the other, return if they meet again"

    p1: tuple[int, int, str] | None = orig_row, orig_col, orig_facing
    p2: tuple[int, int, str] | None = orig_row, orig_col, orig_facing

    flag = False

    while p1 and p2:
        if flag:
            # Only advance every two turns
            p1 = advance(*p1)

        p2 = advance(*p2)
        flag = not flag

        if p1 == p2:
            return True

    return False


def part2():
    global grid, ROWS, COLS, GUARD_COL, GUARD_ROW
    row, col = GUARD_ROW, GUARD_COL
    facing = "up"

    # Needs to be unique
    blocking_points = set()

    # Must advance once
    result = advance(row, col, facing)

    while result is not None:
        new_row, new_col, new_facing = result
        if facing == new_facing:
            # What if it were blocked
            grid[new_row][new_col] = "#"
            if would_loop(row, col, rotate_face(facing)):
                blocking_points.add((new_row, new_col))
            grid[new_row][new_col] = "."

        row, col, facing = result
        result = advance(*result)

    return len(blocking_points)


def main():
    # part1()
    part2()
    pass


if __name__ == "__main__":
    main()
