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


def is_in_bounds(row, col) -> bool:
    "Whether or not with in bounds"
    return 0 <= row < ROWS and 0 <= col < COLS


def rotate_right(facing):
    return ROTATE_RIGHT[facing]


def look_ahead(row, col, facing):
    r, c = TO_ADD[facing]
    return row + r, col + c


def step(row, col, facing):
    new_row, new_col = look_ahead(row, col, facing)

    if not is_in_bounds(new_row, new_col):
        return None

    if grid[new_row][new_col] == "#":
        facing = rotate_right(facing)
    else:
        row, col = new_row, new_col

    return row, col, facing


def part1():
    "Advance and mark the grid with X's, if stepped on something that isn't X, count it"
    row, col = GUARD_ROW, GUARD_COL
    facing = "UP"

    count = 1  # guard start pos
    grid[row][col] = "X"

    while (result := step(row, col, facing)) is not None:
        row, col, facing = result
        if grid[row][col] != "X":
            grid[row][col] = "X"
            count += 1

    return count


def does_loop(row, col, facing):
    "Given guard row col and facing, check if will loop"
    p1 = row, col, facing
    p2 = row, col, facing

    flag = False

    while p1 and p2:
        if flag:
            p1 = step(*p1)

        flag = not flag
        p2 = step(*p2)
        if p1 == p2:
            return True

    return False


def part2():
    "Advance and check every time what if there were a block ahead"
    row, col = GUARD_ROW, GUARD_COL
    facing = "UP"

    points = set()
    bad_points = {(row + r, col + c) for r, c in TO_ADD.values()}
    bad_points.add((row, col))

    while (result := step(row, col, facing)) is not None:
        next_row, next_col = look_ahead(row, col, facing)
        if grid[next_row][next_col] != "#":
            grid[next_row][next_col] = "#"

            if does_loop(row, col, facing):
                points.add((next_row, next_col))

            grid[next_row][next_col] = "."

        row, col, facing = result

    resulting_points = points - bad_points
    total = len(resulting_points)
    return total


def main():
    # part1()
    part2()
    pass


if __name__ == "__main__":
    main()
