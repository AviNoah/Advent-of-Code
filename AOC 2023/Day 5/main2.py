class conversion_map:
    def __init__(
        self, key_name: str, value_name: str, ranges: list[int, int, int] = list()
    ):
        self.key_name: str = key_name
        self.value_name: str = value_name
        self.ranges: list[int, int, int] = ranges

    def get_value(self, key: int) -> int:
        # If value is in any of the ranges, return value, if not return key
        for d_st, s_st, rng_len in self.ranges:
            if d_st <= key < d_st + rng_len:
                diff = key - d_st
                return s_st + diff  # Return new value
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
