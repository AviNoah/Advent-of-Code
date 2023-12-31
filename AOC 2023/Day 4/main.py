# Card X: winning set | lotted numbers
# Point calculation: 2^(n-1) where n is the amount of matching winning numbers from the lot or 0

import re
from collections import deque

with open("input.txt", "r") as f:
    lines: list = f.readlines()

number_pattern: str = r"(\d+)"
number_pattern: re.Pattern = re.compile(number_pattern)


class card:
    def __init__(self, id: int, winning_set: list, lottery_set: list):
        self.id = int(id)
        self.winning_set = winning_set
        self.lottery_set = lottery_set

    def get_winning_lots(self) -> list:
        winning_lots: list = [
            lot for lot in self.lottery_set if lot in self.winning_set
        ]
        return winning_lots

    def calculate_score(self) -> int:
        power = len(self.get_winning_lots()) - 1
        if power < 0:
            return 0
        return 2**power

    def __str__(self):
        lots = self.get_winning_lots()
        return f"Card {self.id} has {len(lots)} winning numbers ({', '.join(lots)}), so it is worth {self.calculate_score()} points."


def get_cards() -> list:
    def get_card(line: str) -> card:
        c_id, lots = line.split(":", maxsplit=1)
        c_id = number_pattern.search(c_id).group()  # Get id
        win_lots, drawn_lots = lots.split("|", maxsplit=1)

        win_lots = number_pattern.findall(win_lots)
        drawn_lots = number_pattern.findall(drawn_lots)

        return card(c_id, win_lots, drawn_lots)

    cards: list = [get_card(line) for line in lines]
    return cards


def count_packs(cards: list[card]) -> int:
    # Use deque for easy and quick insert
    # copy, make a list of winning lots count and count of copies
    copies: list = [1 for _ in cards]

    for i, card in enumerate(cards):
        lot_win = len(card.get_winning_lots())
        print(f"{copies[i]} copies of card {i+1}")

        for j in range(1, lot_win + 1):
            index = min(len(copies) - 1, i + j)
            copies[index] += copies[i]  # Make a copy

    return sum(copies)


def sum_points(cards: list[card]) -> int:
    return sum(c.calculate_score() for c in cards)


if __name__ == "__main__":
    cards: list[card] = get_cards()
    # Solution 15268
    print(f"sum is: {sum_points(cards)}")
    # Solution 6283755
    print(f"count is: {count_packs(cards)}")
