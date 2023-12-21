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
        if self.is_value_in_range(key):
            diff = key - self.src_start
            return diff + self.dest_start
        return None

    def intersect(self, other) -> list:
        # Intersect one range with another, meaning pass self's values into other's keys, return
        # a list of ranges where the sources are self's source, and the destinations are other's destination
        raise NotImplementedError
