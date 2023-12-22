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

    def compare_uniques(self, other) -> bool | None:
        # Compare uniques with another, return True if self's type is better, false if it is lesser,
        # or None if it is equal
        global wild_cards
        s_uniq: dict = self.count_uniques()
        o_uniq: dict = other.count_uniques()

        while len(s_uniq) != 0 and len(o_uniq) != 0:
            # Keys
            key_s_uniq: str = max(s_uniq, key=s_uniq.get)
            key_o_uniq: str = max(o_uniq, key=o_uniq.get)

            s_val: int = s_uniq[key_s_uniq]
            o_val: int = o_uniq[key_o_uniq]

            if wild_cards:
                # Make sure no duplicates are added if the key is already J
                # Turn J's into USED wild cards if they are used
                if key_s_uniq != "J" and "J" in s_uniq.keys():
                    s_val += s_uniq.get("J", 0)
                    s_uniq["1"] = s_uniq.pop("J")  # Wild cards have been used

                if key_o_uniq != "J" and "J" in o_uniq.keys():
                    o_val += o_uniq.get("J", 0)
                    o_uniq["1"] = o_uniq.pop("J")  # Wild cards have been used

            # Check if it has a higher rank by having more uniques
            if s_val > o_val:
                return True
            elif o_val > s_val:
                return False

            # Same count of uniques, check for sub uniques
            s_uniq.pop(key_s_uniq)
            o_uniq.pop(key_o_uniq)

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

    part1()  # Same logic


def main():
    part1()  # Solution was 249638405
    part2()  # Prev solution was 250912312


if __name__ == "__main__":
    main()
