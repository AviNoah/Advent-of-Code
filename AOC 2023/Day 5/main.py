def main():
    return


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


def transform(map1: dict, map2: dict) -> dict:
    # Given map1 and map2, search for map1 values as keys in map2,
    # and return corresponding map1 keys : map2 values

    # Discard anything but map1 key and value
    return make_map_to_dict(
        map(lambda d1_k, d1_v, *_: {d1_k: map2.get(d1_v)}, map1, map2)
    )


if __name__ == "__main__":
    map1 = make_map(1, 10, 10)
    print(map1)
    map2 = make_map(10, 50, 10)
    print(map2)
    map3 = transform(map1, map2)
    print(map3)
    main()
