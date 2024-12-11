with open("input.txt", "r") as f:
    data: str = f.read()
    rules, updates = data.split("\n\n", maxsplit=1)
    rules_lines = rules.split()
    updates_lines = updates.split()

    rules_data: dict[str, set[str]] = dict()
    for line in rules_lines:
        a, b = line.split("|")
        if a not in rules_data:
            rules_data[a] = {b}
        rules_data[a].add(b)

    updates_data: list[list] = []
    for line in updates_lines:
        items = line.split(",")
        updates_data.append(items)


def part1() -> None:
    global rules_data, updates_data
    correct_middles: list[int] = []

    def is_valid_update(updates: list[str]) -> bool:
        nonlocal correct_middles
        printed: set[str] = set()

        for update in updates:
            # check if can print
            pages_not_to_print = rules_data.get(update, set())
            if printed.intersection(pages_not_to_print):
                # bad page, stop
                return False
            # good page, print
            printed.add(update)

        return True

    for updates in updates_data:
        if is_valid_update(updates):
            correct_middles.append(int(updates[len(updates) // 2]))

    total = sum(correct_middles)
    pass


def part2():
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
