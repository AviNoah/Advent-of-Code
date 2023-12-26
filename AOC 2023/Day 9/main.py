# Each line is the history of a value
# The difference between each value will generate a new series, get its difference
# Repeat until all are zeros.
# To estimate a new number, we will add a zero, which will add a number to the series above it and so on.
# This will be called Extrapolation.
# Sum all extrapolated values.

# This seems like a discrete polynomial function of power N, meaning we will have to derive N times to reach all 0's


with open("input.txt", "r") as f:
    lines: list = f.readlines()


def get_histories() -> list[list]:
    # Return a list of value histories
    histories: list[list] = [line.replace("\n", "").split(" ") for line in lines]

    def convert_all_to_ints(values: list) -> list:
        return [int(v) for v in values]

    histories: list[list] = [convert_all_to_ints(h) for h in histories]
    return histories


def derive(series: list) -> list:
    return [series[i + 1] - series[i] for i in range(len(series) - 1)]


def extrapolate(series: list) -> int:
    # Extrapolate series, return next number
    if all([s == 0 for s in series]):
        return 0

    diff = derive(series)[-1]
    return series[-1] + diff


def part1():
    histories: list[list] = get_histories()
    results = [extrapolate(history) for history in histories]

    print(results)


def main():
    part1()


if __name__ == "__main__":
    main()
