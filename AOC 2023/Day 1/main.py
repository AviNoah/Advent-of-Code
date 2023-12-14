def main(real_ans: int, do_tests: bool = False):
    with open("input.txt", "r") as file:
        lines: list = file.readlines()

    if do_tests:
        lines: list = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]

    numeric_dig = {
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

    numeric_names = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    numeric_names_reversed = {
        "eno": 1,
        "owt": 2,
        "eerht": 3,
        "ruof": 4,
        "evif": 5,
        "xis": 6,
        "neves": 7,
        "thgie": 8,
        "enin": 9,
    }

    numeric_normal: dict = dict(numeric_dig)
    numeric_normal.update(numeric_names)
    numeric_reversed: dict = dict(numeric_dig)
    numeric_reversed.update(numeric_names_reversed)

    def extract_values(line: str) -> int:
        # Extract first and second digits from the line, return as int
        line: str = line.lower()  # make Lower case

        # Find indices
        number_indices: list = [
            (line.index(dig), val) for dig, val in numeric_normal.items() if dig in line
        ]

        f_dig = min(number_indices, key=lambda x: x[0])[1]  # Find smallest index

        # to find the right most index, we will reverse the string
        line = line[::-1]  # Reverse string

        number_indices: list = [
            (line.index(dig), val)
            for dig, val in numeric_reversed.items()
            if dig in line
        ]

        l_dig = min(number_indices, key=lambda x: x[0])[1]  # Find largest index

        result: int = f_dig * 10 + l_dig
        return result

    lines: list = [extract_values(line) for line in lines]
    total = sum(lines)
    print(f"Sum is: {total}")
    print(f"Real ans is: {real_ans}")


if __name__ == "__main__":
    main(real_ans=54530, do_tests=False)
