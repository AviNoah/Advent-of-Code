def get_sequences() -> list[str]:
    with open("input.txt", "r") as f:
        data = f.read()

    return data.split(",")


def xmas_hash(text: str):
    hash_value: int = 0
    for char in text:
        hash_value += ord(char)

        hash_value *= 17

        hash_value %= 256

    return hash_value


def part1():
    sequences = get_sequences()
    results = [xmas_hash(seq) for seq in sequences]
    print(sum(results))


def main():
    part1()


if __name__ == "__main__":
    main()
