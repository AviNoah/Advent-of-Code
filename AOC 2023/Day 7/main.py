card_types: list = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_dict: list = [(type, i) for i, type in enumerate(card_types)]
card_dict: dict = dict(card_dict)

import re

with open("input.txt", "r") as f:
    lines: list = f.readlines()


class hand:
    def __init__(self, cards: list[str], bid: int):
        self.cards = cards
        self.bid = bid

    def count_uniques(self):
        # A hand is a list of 5 cards
        # Return a dictionary that shows how many times each card appears
        uniques: dict = dict()
        for card in self.cards:
            if not card in uniques.keys():
                uniques[card] = 0  # Initialize

            uniques[card] += 1

        return max(uniques.values())

    def __eq__(self, other):
        # Both have same unique card counts, and have the same cards
        return self.cards == other.cards

    def __gt__(self, other):
        global card_dict
        s_uniq = self.count_uniques()
        o_uniq = other.count_uniques()
        if o_uniq >= s_uniq:
            return False
        elif s_uniq > o_uniq:
            return True

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
    print(hands)


def main():
    part1()


if __name__ == "__main__":
    main()
