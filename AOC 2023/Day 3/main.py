import re

pattern = r"(\d+)"

non_special = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}


def get_values() -> list:
    with open("input.txt", "r") as f:
        lines = f.readlines()

    rows_matches = [re.finditer(pattern, line) for line in lines]

    results: list = list()

    for i, row in enumerate(rows_matches):
        for match in row:
            value: int = int(match.group(1))  # Get value
            st, ed = match.start(), match.end()
            # Check if value is surrounded by a symbol that is not a digit or period
            if any(
                [
                    bool(lines[x][y] not in non_special)
                    for x in range(st - 1, ed + 1)
                    for y in range(i - 1, i + 1)
                ]
            ):
                results.append(value)

    return results


if __name__ == "__main__":
    print(sum(get_values()))
