import re

with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()


class conversion_range:
    def __init__(self, dest_start: int, src_start: int, range_length: int):
        # I will be referring to src as key and dest as value in this code

        self.dest_start = dest_start
        self.dest_end = dest_start + range_length
        self.src_start = src_start
        self.src_end = src_start + range_length
        self.length = range_length

    def is_key_in_range(self, key: int) -> bool:
        # Return whether key is in [self.src_start, self.src_end)
        return bool(self.src_start <= key < self.src_end)

    def is_value_in_range(self, value: int) -> bool:
        # Return whether key is in [self.dest_start, self.dest_end)
        return bool(self.dest_start <= value < self.dest_end)

    def get_key(self, value: int) -> int | None:
        # Get key matching value
        if self.is_value_in_range(value):
            diff = value - self.dest_start
            return diff + self.src_start
        return None

    def get_value(self, key: int) -> int | None:
        # Get value matching key
        if self.is_key_in_range(key):
            diff = key - self.src_start
            return diff + self.dest_start
        return None

    def intersect(self, other) -> list:
        # Intersect one range with another, meaning pass self's values into other's keys, return
        # a list of ranges where the sources are self's source, and the destinations are other's destination
        raise NotImplementedError

    def to_str_with_padding(self, padding: int) -> str:
        padded = "{:<{}} {:<{}} {:<{}}".format(
            self.dest_start, padding, self.src_start, padding, self.length, padding
        )
        return padded


class conversion_map:
    def __init__(
        self, key_name: str, value_name: str, ranges: list[conversion_range] = list()
    ):
        self.key_name: str = key_name
        self.value_name: str = value_name
        self.ranges: list[conversion_range] = ranges

    def get_full_name(self) -> str:
        return f"{self.key_name}-to-{self.value_name}"

    def get_key(self, value: int) -> int:
        # Search in ranges for key matching value, if none found, return value
        for range in self.ranges:
            key = range.get_key(value)
            if not key is None:
                return key

        return value

    def get_value(self, key: int) -> int:
        # Search in ranges for value matching key, if none found, return key
        for range in self.ranges:
            value = range.get_value(key)
            if not value is None:
                return value

        return key

    def get_local_min_key(self) -> conversion_range:
        # Return locally minimum key
        range: conversion_range = min(self.ranges, key=lambda x: x.src_start)
        return range.src_start

    def get_local_min_value(self) -> conversion_range:
        # Return locally minimum key
        range: conversion_range = min(self.ranges, key=lambda x: x.dest_start)
        return range.dest_start

    @staticmethod
    def from_line(key_name: str, value_name: str, data: str):
        # Data is a big string containing multiples of number triplets
        data = data.replace("\n", "")  # Remove line breaks
        data: list[str] = data.split(" ")
        data: list[int] = [int(s) for s in data if s != ""]  # Convert to ints

        # Group every 3 numbers together, this is a separate range data
        data: list[list[int]] = group_elements(data, 3)
        data: list[list[int]] = sorted(data, key=lambda r: r[1])  # Sort by source

        data: list[conversion_range] = [conversion_range(*d) for d in data]
        return conversion_map(key_name, value_name, data)

    def __str__(self) -> str:
        # Name
        result: str = self.get_full_name() + "\n"

        # Padding for key and values
        padding = len(self.get_full_name())

        # Key value names
        result += (
            "{:<{}} {:<{}}".format(
                str(self.key_name), padding, str(self.value_name), padding
            )
            + "\n"
        )

        # Values
        for range in self.ranges:
            padded = range.to_str_with_padding(padding)
            result += f"{padded}\n"

        return result


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


def get_seeds() -> list[int]:
    # Return a list of seeds, each entry contains one seed
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

    maps: list[conversion_map] = [
        conversion_map.from_line(match.group(1), match.group(2), match.group(3))
        for match in maps
    ]

    return maps


def part1():
    seeds: list[int] = get_seeds()
    maps: list[conversion_map] = get_maps()

    def transform_seed(seed: int) -> int:
        # Given a seed, convert it in the conversion map list until it is exhausted, return final result
        for map in maps:
            tmp = map.get_value(seed)
            seed = tmp

        return seed

    results: list[int, int] = [(seed, transform_seed(seed)) for seed in seeds]

    lowest_loc: tuple = min(results, key=lambda x: x[1])
    print(f"Lowest location is {lowest_loc[1]} for seed {lowest_loc[0]}")


def part2():
    ...


def main():
    part1()  # Solution is 379811651
    #  part2()  # Prev ans: 222541566


if __name__ == "__main__":
    main()
