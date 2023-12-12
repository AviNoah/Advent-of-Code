def main(do_tests: bool = False):
    with open("input.txt", "r") as file:
        lines: list = file.readlines()

    if do_tests:
        lines: list = ["1abc2five", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

    numeric_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    def extract_values(line: str) -> int:
        # Extract first and second digits from the line, return as int
        line: str = line.lower()  # make Lower case

        # Find indices
        number_indices: list = [
            (line.index(dig), val) for dig, val in numeric_dict.items() if dig in line
        ]

        f_dig = min(number_indices, key=lambda x: x[0])[1]  # Find smallest index
        l_dig = max(number_indices, key=lambda x: x[0])[1]  # Find largest index

        return f_dig * 10 + l_dig

    lines: list = [extract_values(line) for line in lines]
    total = sum(lines)
    print(f"Sum is: {total}")


if __name__ == "__main__":
    main(do_tests=True)
