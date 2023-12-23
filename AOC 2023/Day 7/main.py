card_types: list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_dict: list = [(type, i) for i, type in enumerate(card_types)]
card_dict: dict = dict(card_dict)

wild_cards: bool = False

import re

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class hand:
    def __init__(self, cards: list[str], bid: int):
        self.cards = cards
        self.bid = int(bid)

    def count_uniques(self) -> dict:
        # A hand is a list of 5 cards
        # Return a dictionary that shows how many times each card appears
        uniques: dict = dict()
        for card in self.cards:
            if not card in uniques.keys():
                uniques[card] = 0  # Initialize

            uniques[card] += 1

        return uniques

    def evaluate_type(self) -> int:
        # Return type of hand
        # High-0; one-1; two-2; three-3; full-house-4; four-5; five-6
        global wild_cards
        d: dict = self.count_uniques()
        key = max(d, key=d.get)

        j_tmp = 0
        if wild_cards and "J" in d.keys():
            j_tmp = d.pop("J")
            if j_tmp == 5:
                return 6

            # Get new max key
            key = max(d, key=d.get)

            # Join rest of code

        # We no longer need to care about J

        return_val: int = d.pop(key) + j_tmp
        if not d:
            # Dict is empty, meaning everything is the same character, even if there is J the result will be 5.
            return 6  # Five of a kind

        if return_val == 4:
            return 5  # Four of a kind

        sub_max_key = max(d, key=d.get)
        sub_val = d[sub_max_key]

        if sub_val == 2 and return_val == 3:
            return 4  # Full house

        if return_val == 3:
            return 3  # Three of a kind

        if sub_val == 2 and return_val == 2:
            return 2  # Two pair

        if return_val == 2:
            return 1  # One pair

        return 0  # High card

    def compare_uniques(self, other) -> bool | None:
        # Compare uniques with another, return True if self's type is better, false if it is lesser,
        # or None if it is equal
        # Check type
        s_val = self.evaluate_type()
        o_val = other.evaluate_type()

        if s_val > o_val:
            return True
        elif o_val > s_val:
            return False
        return None

    def __eq__(self, other):
        # Both have same unique card counts, and have the same cards
        return self.cards == other.cards

    def __gt__(self, other):
        global card_dict

        result = self.compare_uniques(other)
        if result is not None:
            return result

        for c1, c2 in zip(self.cards, other.cards):
            if card_dict[c1] > card_dict[c2]:
                return True
            elif card_dict[c1] < card_dict[c2]:
                return False
        return False  # They are equal

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return other > self

    def __le__(self, other):
        return other > self or self == other


def get_hands() -> list[hand]:
    global lines
    hand_pattern = r"([\d\S]+) (\d+)"
    hands: list[re.Match] = [re.match(hand_pattern, line) for line in lines]
    hands: list[hand] = [hand(match.group(1), match.group(2)) for match in hands]

    return hands


def part1():
    hands: list[hand] = get_hands()
    hands: list[hand] = sorted(hands)

    payout: list[int] = [hand.bid * (i + 1) for i, hand in enumerate(hands)]
    print(sum(payout))


def part2():
    global card_dict, wild_cards
    card_types: list = [
        "1",
        "J",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "T",
        "Q",
        "K",
        "A",
    ]
    # J cards are now wild cards who can INCREASE RANK by changing the hand's type
    # "1" cards don't really exist, they are meant to represent USED wild cards

    wild_cards = True
    card_dict = [(type, i) for i, type in enumerate(card_types)]
    card_dict = dict(card_dict)

    # Give them both the same value
    card_dict["1"] = card_dict["J"]

    part1()  # Same logic


def main():
    part1()  # Solution was 249638405
    part2()  # Solution was 249776650


if __name__ == "__main__":
    main()
