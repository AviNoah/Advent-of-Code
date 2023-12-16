def main():
    return


# Define map monad, we want to be able to trace changes as well
class my_map:
    def __init__(
        self,
        map: dict,
        map_name: str,
        key_name: str,
        value_name: str,
        logs: list = list(),
    ):
        self.map: dict = map
        self.map_name = map_name
        self.key_name = key_name
        self.value_name = value_name
        self.logs: list = logs

    def transform(self, map2: dict):
        # Given map1 and map2, search for map1 values as keys in map2,
        # and return corresponding map1 keys : map2 values in a my_map monad

        # Discard anything but map1 key and value
        tmp_dict: dict = self.make_map_to_dict(
            map(lambda d1_k, d1_v, *_: {d1_k: map2.get(d1_v)}, map1, map2)
        )


def make_map_to_dict(my_map: map) -> dict:
    # Convert map into dict.
    my_dict: dict = dict()
    for KV in my_map:
        my_dict.update(KV)

    return my_dict


def make_map(
    destination_range_start: int, source_range_start: int, range_length: int
) -> dict:
    # Map the first range_length numbers, counting from destination_range_start to the first
    # range_length numbers, counting from source_range_start.
    # Including the starts and excluding start + length

    dest_rng: range = range(
        destination_range_start, destination_range_start + range_length
    )
    source_rng: range = range(source_range_start, source_range_start + range_length)

    # Add dictionary keys as values and convert to dict
    return make_map_to_dict(map(lambda a, b: {a: b}, dest_rng, source_rng))


if __name__ == "__main__":
    map1: my_map = my_map(make_map(1, 10, 10), "seed-to-soil", "seed", "soil")
    print(map1)
    map2: my_map = my_map(
        make_map(10, 50, 10), "soil-to-fertilizer", "soil", "fertilizer"
    )
    print(map2)
    map3: my_map = map1.transform(map2)
    print(map3)
    main()
