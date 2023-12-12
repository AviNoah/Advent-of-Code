def main(do_tests: bool = False):
    with open("input.txt", "r") as file:
        lines: list = file.readlines()

    if do_tests:
        lines: list = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

    def extract_values(line: str) -> int:
        # Extract first and second digits from the line, return as int
        Min_number_indices: list = [
            line.index(str(num)) for num in range(10) if str(num) in line
        ]
        f_dig = min(Min_number_indices)
        reversed_line: str = line[::-1]
        Max_number_indices: list = [
            reversed_line.index(str(num))
            for num in range(10)
            if str(num) in reversed_line
        ]
        l_dig = min(Max_number_indices)

        return int(line[f_dig] + reversed_line[l_dig])

    lines: list = [extract_values(line) for line in lines]
    total = sum(lines)
    print(f"Sum is: {total}")


if __name__ == "__main__":
    main(do_tests=False)
