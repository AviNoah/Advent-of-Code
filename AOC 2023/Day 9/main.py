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
    print(histories)


def derive(series: list) -> list:
    series = series[:]  # Make copy
    *series, end = series

    return [series[i + 1] - elem for i, elem in enumerate(series)]


def main():
    histories: list[list] = get_histories()
    for history in histories:
        print(history)
        print(derive(history))


if __name__ == "__main__":
    main()
