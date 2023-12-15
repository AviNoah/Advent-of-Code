import re

digit_pattern = r"(\d+)"
asterisk_pattern = r"\*"
non_special = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "\n"}

with open("input.txt", "r") as f:
    lines = f.readlines()

# We will find all values using regex, and then check in a rectangular grid around them if they contain a special symbol,
# this prevents duplicates and more efficient


class part:
    def __init__(self, value: int, st: int, ed: int):
        self.value = int(value)
        self.st = st
        self.ed = ed

    def does_overlap(self, _range: range) -> bool:
        # Given range, check if st and ed are within it, _range has steps of 1.
        return self.st in _range or self.ed in _range


def get_value(row: int, col: int) -> str:
    if 0 <= row < len(lines) and 0 <= col < len(lines[row]):
        return lines[row][col]
    return "."  # This counts as just false


def match_from_file(pattern) -> list:
    # Return a list of rows which each contain a list of parts found in them

    global lines
    rows_matches = [re.finditer(pattern, line) for line in lines]
    return rows_matches


def get_parts() -> list:
    # Return a list of rows which each contain a list of valid parts found in them
    rows_matches = match_from_file(digit_pattern)
    results: list = list()

    for i, row_match in enumerate(rows_matches):
        row_results = list()
        for match in row_match:
            value: int = int(match.group(1))  # Get value
            st, ed = (
                match.start(),
                match.end(),
            )  # end returns the char just after the match
            # Check if value is surrounded by a symbol that is not a digit or period
            if any(
                [
                    bool(get_value(row, col) not in non_special)
                    for col in range(st - 1, ed + 1)  # between st-1 and ed inclusive
                    for row in range(i - 1, i + 2)  # between i-1 and i+1 inclusive
                ]
            ):
                row_results.append(part(value, st, ed))
        results.append(row_results)

    return results


def get_gear_parts() -> list:
    # A gear is an asterisk symbol that is near exactly 2 gear parts
    # a gear part is a number near a gear

    parts_rows = get_parts()
    asterisk_rows = match_from_file(asterisk_pattern)

    gear_parts: list = list()

    for i, row in enumerate(asterisk_rows):
        for match in row:
            rng = range(match.start(), match.end() + 1)
            overlapping_parts = [
                part
                for j in range(i - 1, i + 2)
                for part in parts_rows[j]
                if part.does_overlap(rng)
            ]

            gear_parts.append(overlapping_parts)

    # Ignore if not exactly two
    gear_parts = [part for part in gear_parts if len(part) == 2]

    return gear_parts


def sum_parts(parts_tables: list[list]) -> int:
    return sum(part.value for part_row in parts_tables for part in part_row)


def sum_gear_ratios(gears: list[list]) -> int:
    return sum(row[0].value * row[1].value for row in gears)


if __name__ == "__main__":
    parts = get_parts()
    gear_parts = get_gear_parts()
    # Sol 560670
    print(sum_parts(parts))
    print(sum_gear_ratios(gear_parts))
