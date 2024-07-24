import re


def get_sequences() -> list[str]:
    with open("input.txt", "r") as f:
        data = f.read()

    return data.split(",")


def HASH(text: str) -> int:
    hash_value: int = 0
    for char in text:
        hash_value += ord(char)

        hash_value *= 17

        hash_value %= 256

    return hash_value


class Lens:
    label: str
    value: int

    def __init__(self, label: str, value: int) -> None:
        self.label = label
        self.value = value

    def lens_power(self, box_num_plus_1: int, slot_num: int) -> int:
        # Both parameters are 1-indexed
        return box_num_plus_1 * slot_num * self.value

    def __eq__(self, other):
        if isinstance(other, Lens):
            return self.label == other.label
        return False

    def __hash__(self):
        return hash(self.label)

    def __str__(self) -> str:
        return f"[{self.label} {self.value}]"

    def __repr__(self) -> str:
        return self.__str__()


def part1():
    sequences = get_sequences()
    results = [HASH(seq) for seq in sequences]
    print(sum(results))


def part2() -> None:
    def HASHMAP(text: str) -> None:
        result = re.match(r"(\w+)([-=])(\d)*", text)

        if result is None:
            raise ValueError("Bad text %s", text)

        label: str
        operation: str
        strength_str: str | None

        label, operation, strength_str = result.groups()

        box_num: int = HASH(label)
        box: list[Lens] = boxes[box_num]

        if operation == "-":
            # Lens focal strength doesn't matter
            lens = Lens(label, 1)
            if lens in box:
                box.remove(lens)
        else:
            strength = int(strength_str)
            lens = Lens(label, strength)
            try:
                index: int = box.index(lens)
                box.pop(index)
                box.insert(index, lens)
            except ValueError:
                # simply insert
                box.append(lens)

    sequences = get_sequences()
    boxes: list[list[Lens]] = [[] for _ in range(256)]

    for seq in sequences:
        HASHMAP(seq)

    lens_power: int = 0

    for box_num_plus_1, lens_box in enumerate(boxes, start=1):
        lens_power += sum(
            [
                lens.lens_power(box_num_plus_1, slot)
                for slot, lens in enumerate(lens_box, start=1)
            ]
        )
    print(lens_power)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
