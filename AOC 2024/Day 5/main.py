from collections import deque


with open("input.txt", "r") as f:
    data: str = f.read()
    rules, pages = data.split("\n\n", maxsplit=1)
    rules_lines = rules.split()
    pages_lines = pages.split()

    rules_data: dict[str, set[str]] = dict()
    for line in rules_lines:
        a, b = line.split("|")
        if a not in rules_data:
            rules_data[a] = {b}
        rules_data[a].add(b)

    pages_data: list[list] = []
    for line in pages_lines:
        items = line.split(",")
        pages_data.append(items)


def is_valid_update(pages: list[str]) -> bool:
    printed: set[str] = set()

    for page in pages:
        # check if can print
        pages_not_to_print = rules_data.get(page, set())
        if printed.intersection(pages_not_to_print):
            # bad page, stop
            return False
        # good page, print
        printed.add(page)

    return True


def part1() -> None:
    global rules_data, pages_data
    correct_middles: list[int] = []

    for pages in pages_data:
        if is_valid_update(pages):
            correct_middles.append(int(pages[len(pages) // 2]))

    total = sum(correct_middles)
    pass


def part2() -> None:
    global pages_data, rules_data
    invalids = [pages for pages in pages_data if not is_valid_update(pages)]

    def fix_pages(pages: list[str]) -> list[str]:
        printed_set: set[str] = set()
        printed_stack: list[str] = []

        for page in pages:
            bad_pages = rules_data.get(page, set())
            removed = []
            while printed_stack and printed_set.intersection(bad_pages):
                popped = printed_stack.pop()
                printed_set.remove(popped)
                removed.append(popped)

            printed_set.add(page)
            printed_stack.append(page)

            printed_set.update(removed)
            printed_stack.extend(reversed(removed))

        return printed_stack

    fixed = [fix_pages(pages) for pages in invalids]
    correct_middles = [int(pages[len(pages) // 2]) for pages in fixed]
    total = sum(correct_middles)
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
