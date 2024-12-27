with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()
    grid: list[list] = [list(line.strip()) for line in lines]
    ROWS = len(grid)
    COLS = len(grid[0])


def get_guard_pos():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] not in {".", "#"}:
                return row, col
    raise


GUARD_ROW, GUARD_COL = get_guard_pos()

ROTATE_RIGHT = {"UP": "RIGHT", "RIGHT": "DOWN", "DOWN": "LEFT", "LEFT": "UP"}
TO_ADD = {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}


def rotate_right(facing):
    return ROTATE_RIGHT[facing]


def look_ahead(row, col, facing):
    r, c = TO_ADD[facing]
    return row + r, col + c


def in_bounds(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


def part1():
    row, col, facing = GUARD_ROW, GUARD_COL, "UP"
    next_row, next_col = look_ahead(row, col, facing)
    count = 1  # Include when you are just about to exit the map

    while in_bounds(next_row, next_col):
        if grid[row][col] != "X":
            grid[row][col] = "X"
            count += 1

        if grid[next_row][next_col] == "#":
            facing = rotate_right(facing)
            next_row, next_col = row, col  # Step back

        row, col = next_row, next_col
        next_row, next_col = look_ahead(row, col, facing)

    return count


def does_loop(row, col, facing):
    # Just keep track of every cell, if we go out of the same cell for the same direction
    # twice, we loop.
    visited = {
        "LEFT": set(),
        "RIGHT": set(),
        "UP": set(),
        "DOWN": set(),
    }
    next_row, next_col = look_ahead(row, col, facing)
    while in_bounds(next_row, next_col):

        if grid[next_row][next_col] == "#":
            facing = rotate_right(facing)
            next_row, next_col = look_ahead(row, col, facing)
            continue

        if (row, col) in visited[facing]:
            return True

        visited[facing].add((row, col))

        row, col = next_row, next_col
        next_row, next_col = look_ahead(row, col, facing)

    return False


def part2():
    row, col, facing = GUARD_ROW, GUARD_COL, "UP"
    next_row, next_col = look_ahead(row, col, facing)
    solutions = set()

    # Run normal solution, but check every time we don't turn, if we would've looped
    while in_bounds(next_row, next_col):
        if grid[next_row][next_col] == "#":
            facing = rotate_right(facing)
            next_row, next_col = row, col  # Step back
        else:
            # Place block and check if would loop
            grid[next_row][next_col] = "#"
            if does_loop(row, col, facing):
                solutions.add((next_row, next_col))
            grid[next_row][next_col] = "."

        row, col = next_row, next_col
        next_row, next_col = look_ahead(row, col, facing)

    invalid_solutions = {
        (GUARD_ROW, GUARD_COL),
        (GUARD_ROW + 1, GUARD_COL),
    }
    valid_solutions = solutions - invalid_solutions
    count = len(valid_solutions)
    return count


def main():
    # assert part1() == 5095
    part2()


if __name__ == "__main__":
    main()
