import re

pattern = r"(\d+)"

digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def make_table():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    rows_matches = [re.finditer(pattern, line) for line in lines]

    for i, row in enumerate(rows_matches):
        for match in row:
            value = match.group(1)  # Get value
            print(value)


if __name__ == "__main__":
    make_table()
