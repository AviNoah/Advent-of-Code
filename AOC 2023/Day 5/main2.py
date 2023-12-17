import re

with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()


class conversion_map:
    def __init__(
        self, key_name: str, value_name: str, ranges: list[list[int]] = list()
    ):
        self.key_name: str = key_name
        self.value_name: str = value_name
        self.ranges: list[list[int]] = ranges

    def get_value(self, key: int) -> int:
        # If value is in any of the ranges, return value, if not return key
        for d_st, s_st, rng_len in self.ranges:
            if s_st <= key < s_st + rng_len:
                diff = key - s_st
                return d_st + diff  # Return new value
        return key

    def get_full_name(self) -> str:
        return f"{self.key_name}-to-{self.value_name}"

    def __str__(self) -> str:
        # Name
        result: str = self.get_map_name() + "\n"

        # Padding for key and values
        padding = len(self.get_map_name())

        # Key value names
        result += (
            "{:<{}} {:<{}}".format(
                str(self.key_name), padding, str(self.value_name), padding
            )
            + "\n"
        )

        # Values
        for dest_rg, src_rg, rng in self.ranges:
            padded = "{:<{}} {:<{}} {:<{}}".format(
                dest_rg, padding, src_rg, padding, rng, padding
            )
            result += f"{padded}\n"

        return result


def get_seeds() -> list[int]:
    # Return a list of seeds for lines
    global lines
    full_data: str = "".join(lines).replace("\n", " ")
    seeds_pattern: re.Pattern = re.compile(
        r"seeds:((?:\s\d+)*)"
    )  # Capture all numbers after seeds:

    seeds: re.Match = seeds_pattern.search(full_data)
    seeds: list[int] = [int(s) for s in seeds.group(1).split(" ") if s != ""]

    return seeds


def get_maps() -> list[conversion_map]:
    # Return a list of conversion_maps from lines
    global lines

    full_data: str = "".join(lines).replace("\n", " ")

    map_pattern: re.Pattern = re.compile(
        r"(\w+)-to-(\w+) map:((?:\s*\d+ \d+ \d+\s*)+)"
    )  # Captures key value and entire set of data for the map

    maps: list[re.Match] = map_pattern.finditer(full_data)

    def group_elements(iterable, group_size) -> list[list]:
        # Group elements in groups of group_size, return resulting list[list]
        result = []
        current_group = []

        for element in iterable:
            current_group.append(element)
            if len(current_group) == group_size:
                result.append(current_group)
                current_group = []

        # If there are remaining elements, create a last group
        if current_group:
            result.append(current_group)

        return result

    def map_from_line(key_name: str, value_name: str, data: str) -> conversion_map:
        # Data is a big string containing multiples of number triplets
        data = data.replace("\n", "")  # Remove line breaks
        data: list[str] = data.split(" ")
        data: list[int] = [int(s) for s in data if s != ""]  # Convert to ints

        # Group every 3 numbers together, this is a separate range data
        data: list[list[int]] = group_elements(data, 3)
        return conversion_map(key_name, value_name, data)

    maps: list[conversion_map] = [
        map_from_line(match.group(1), match.group(2), match.group(3)) for match in maps
    ]

    return maps


def transform_seed(
    seed: int, maps: list[conversion_map], print_logs: bool = False
) -> int:
    # Given a seed, convert it in the conversion map list until it is exhausted, return final result
    logs: list = list()

    for map in maps:
        tmp = map.get_value(seed)
        logs.append(f"{map.key_name} {seed} corresponds to {map.value_name} {tmp}")
        seed = tmp

    if print_logs:
        for log in logs:
            print(f"- {log}")

        print()  # Add a line break

    return seed


def transform_seeds(
    seeds: list[int], maps: list[conversion_map], print_logs: bool = False
) -> list[int, int]:
    # Return a list of 2 element tuples containing starting seed and result
    tuples: list[int, int] = [
        (seed, transform_seed(seed, maps, print_logs)) for seed in seeds
    ]
    return tuples


def main():
    seeds: list[int] = get_seeds()
    maps: list[conversion_map] = get_maps()

    results: list[int, int] = transform_seeds(seeds, maps, print_logs=False)

    for seed, result in results:
        print(f"{seed} -> {result}")


if __name__ == "__main__":
    main()
