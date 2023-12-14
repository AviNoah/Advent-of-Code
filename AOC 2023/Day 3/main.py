import re

pattern = r"(\d+)"

non_special = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}

# We will find all values using regex, and then check in a rectanular grid around them if they contain a special symbol,
# this prevents duplicates and more efficient


def get_values() -> list:
    with open("input.txt", "r") as f:
        lines = f.readlines()

    def get_value(row: int, col: int) -> str:
        if 0 <= row < len(lines) and 0 <= col < len(lines[0]):
            return lines[row][col]
        return "."  # This counts as just false

    rows_matches = [re.finditer(pattern, line) for line in lines]

    results: list = list()

    for i, row_match in enumerate(rows_matches):
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
                    for col in range(st - 1, ed + 1)  # between st-1 and ed+1 exclusive
                    for row in range(i - 1, i + 2)  # between i-1 and i+1 inclusive
                ]
            ):
                results.append(value)

    return results


if __name__ == "__main__":
    vals = get_values()
    print(sum(vals))
