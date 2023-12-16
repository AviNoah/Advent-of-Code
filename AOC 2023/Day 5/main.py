def main():
    return


def make_map(
    destination_range_start: int, source_range_start: int, range_length: int
) -> map:
    # Map the first range_length numbers, counting from destination_range_start to the first
    # range_length numbers, counting from source_range_start.
    # Including the starts and excluding start + length

    dest_rng: range = range(
        destination_range_start, destination_range_start + range_length
    )
    source_rng: range = range(source_range_start, source_range_start + range_length)

    # Add dictionary keys as values
    return map(lambda a, b: {a: b}, dest_rng, source_rng)


if __name__ == "__main__":
    main()
